from django.core.mail import send_mail
from django.conf import settings
import random
import string


def generate_otp(length=4):
    characters = string.digits
    otp = "".join(random.choice(characters) for i in range(length))
    return otp


def send_otp_email(email, otp):
    subject = "OTP for account activation"
    message = f"Your OTP for account activation is {otp}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    return True
