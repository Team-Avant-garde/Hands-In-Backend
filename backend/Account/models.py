from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class CustomUserManager(BaseUserManager):
    '''
    A custom user model manager that uses the email as a unique identifier
    for authentication instead of the username
    '''
      
    def create_user(self, username,email, password=None):
        
        if not email:
            raise ValueError("Users must have a valid student email address")
        user = self.model(
            username = username,
            email=self.normalize_email(email),

        )
        user.set_password(password)
        user.save()    
        
        return user

    def create_superuser(self, username,email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username = username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user





class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True,db_index=True)
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

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
    phone_number = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
