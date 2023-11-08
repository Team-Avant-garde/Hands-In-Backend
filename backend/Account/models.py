from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import RegexValidator, validate_email

phone_regex = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message="phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
)


class CustomUserManager(BaseUserManager):
    """
    A custom user model manager that uses the email as a unique identifier
    for authentication instead of the username
    """

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have a valid student email address")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, validators=[validate_email])
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_tries = models.CharField(max_length=2, default=settings.MAX_OTP_TRY)
    otp_max_out = models.DateTimeField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    programme = models.CharField(max_length=255)
    current_level = models.CharField(max_length=100)
    phone_number = models.CharField(
        unique=True, validators=[phone_regex], max_length=17, null=True, blank=True
    )
    profile_picture = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
