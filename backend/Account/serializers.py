from rest_framework import serializers
from datetime import datetime, timedelta
import random
from django.conf import settings
from .utils import send_otp_email


from .models import User

def is_student_email(email):
    # Split email into username and domain
    _, domain = email.split('@', 1)

    # Check if '.edu' is in the domain
    return '.edu' in domain.lower()



class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]

        if is_student_email(email):
            otp = random.randint(1000, 9999)
            otp_expiry = datetime.now() + timedelta(minutes=10)

            user = User(
                username=validated_data["username"],
                email=email,
                otp=otp,
                otp_expiry=otp_expiry,
                max_otp_tries=settings.MAX_OTP_TRY,
            )
            user.set_password(validated_data["password"])
            user.save()
            send_otp_email(validated_data["email"], otp)
            return user
        else:
            # Handle non-student emails as per your requirements
            raise serializers.ValidationError({"email": "Not a valid student email."})


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

class UserOtp(serializers.Serializer):
    userOtp = serializers.CharField(max_length=5)
   
