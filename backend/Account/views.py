from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate
from rest_framework.generics import CreateAPIView

import datetime
import random

from .serializers import UserSignUpSerializer, UserLoginSerializer, UserOtp
from .models import User
from .utils import generate_otp, send_otp_email


class UserSignupView(CreateAPIView):
    serializer_class = UserSignUpSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"user_id": user.id, "username": user.username, "email": user.email},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OtpView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserOtp

    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        instance = self.get_object()

        if (
            not instance.is_active
            and instance.otp == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_active = True
            instance.otp_expiry = None
            instance.max_otp_tries = settings.MAX_OTP_TRY
            instance.otp_max_out = None
            instance.save()

            return Response(
                {"message": "OTP verified successfully"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "User active or please enter a valid OTP"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    @action(detail=True, methods=["PATCH"])
    def resend_otp(self, request, pk=None):
        instance = self.get_object()

        if int(instance.max_otp_tries) == 0 and timezone.now() < instance.otp_max_out:
            return Response(
                {"message": "OTP max out, please try after 10 minutes"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp = random.randint(1000, 9999)
        otp_expiry = timezone.now() + datetime.timedelta(minutes=10)
        max_otp_try = int(instance.max_otp_tries) - 1

        instance.otp = otp
        instance.otp_expiry = otp_expiry
        instance.max_otp_tries = max_otp_try

        if max_otp_try == 0:
            instance.otp_max_out = timezone.now() + datetime.timedelta(minutes=10)
        elif max_otp_try == -1:
            instance.max_otp_try = settings.MAX_OTP_TRY
        else:
            instance.otp_max_out = None
            instance.max_otp_tries = max_otp_try

        instance.save()
        send_otp_email(instance.email, otp)
        return Response(
            {"message": "OTP resent successfully"}, status=status.HTTP_200_OK
        )


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid:
            user = authenticate(
                email=serializer.validated_data["email"],
                password=serializer.validated_data["password"],
            )

            if user:
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({"token": token}, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

        return Response(
            {"message": "Login Successful"}, status=status.HTTP_400_BAD_REQUEST
        )
