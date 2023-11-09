from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register("otp", views.OtpView, basename="otp")
router.register("profile", views.Profile, basename="profile")


urlpatterns = [
    path("signup/", views.UserSignupView.as_view(), name="user_signup"),
    path("login/", views.UserLoginView.as_view(), name="user_login"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]


urlpatterns += router.urls
