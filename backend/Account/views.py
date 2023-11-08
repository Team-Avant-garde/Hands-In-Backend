from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime, timedelta

import datetime
import random

from .serializers import UserSignUpSerializer
from .models import User
from .utils import generate_otp, send_otp_email

class UserSignupView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    # def post(self, request):
    #     user = request.data
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     user_data = serializer.data

    #     return Response(user_data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["PATCH"])
    def verify_otp(self, request, pk=None):
        instance = self.get_object()

        if (
            not instance.is_active
            and instance.opt == request.data.get("otp")
            and instance.otp_expiry
            and timezone.now() < instance.otp_expiry
        ):
            instance.is_Active = True
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
        max_otp_try = int(instance.max_otp_try) - 1

        instance.otp = otp
        instance.otp_expiry = otp_expiry
        instance.max_otp_tries = max_otp_try

        if max_otp_try == 0:
            instance.otp_max_out = timezone.now() + datetime.timedelta(minutes=10)
        elif max_otp_try == -1:
            instance.max_otp_try = settings.MAX_OTP_TRY
        else:
            instance.otp_max_out = None
            instance.max_otp_try = max_otp_try
        
        instance.save()
        send_otp_email(instance.email, otp)
        return Response({"message": "OTP resent successfully"}, status=status.HTTP_200_OK)
