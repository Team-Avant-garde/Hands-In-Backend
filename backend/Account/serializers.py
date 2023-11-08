from rest_framework import serializers
from datetime import datetime, timedelta
import random
from django.conf import settings
from .utils import send_otp_email
from django.contrib.auth import authenticate

from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes=10)

        user = User(
            username=validated_data["username"],
            email=validated_data["email"],
            otp=otp,
            otp_expiry=otp_expiry,
            max_otp_tries=settings.MAX_OTP_TRY,
        )
        user.set_password(validated_data["password"])
        user.save()
        send_otp_email(validated_data["email"], otp)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

    def validate(self,data):
        validated_data = super().validate(data)

        email = validated_data.get('email')
        password = validated_data.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password")
        
        return user
