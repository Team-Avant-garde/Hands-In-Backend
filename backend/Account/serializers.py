from rest_framework import serializers
from datetime import datetime, timedelta
import random
from django.conf import settings
from .utils import send_otp_email
import re
from . models import Profile

from .models import User

def is_student_email(email):
    # Split email into username and domain
    _, domain = email.split('@', 1)

    # Check if '.edu' is in the domain
    return '.edu' in domain.lower()


### Checks for strong Password
def validate_password(password):
    """
    Check if the password is strong enough
    """
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'\d', password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}|:"<>?~\-=\[\]\\;\',./]', password):
        return False

    return True



class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]

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
            if validate_password(password):
                user.set_password(password)
                user.save()
                send_otp_email(validated_data["email"], otp)
                return user
            else:
                raise serializers.ValidationError({"password": "Not a strong password"})
        else:
            # Handle non-student emails as per your requirements
            raise serializers.ValidationError({"email": "Not a valid student email."})


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=100, write_only=True)

class UserOtp(serializers.Serializer):
    userOtp = serializers.CharField(max_length=5)
   

class ProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects. """
    class Meta:
        model = Profile
        fields = ['user', 'firstname', 'lastname', 'programme', 'current_level', 'phone_number', 'profile_picture','bio']