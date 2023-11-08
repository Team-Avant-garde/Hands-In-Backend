from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserSignupView, basename="user")


urlpatterns = [ 
    path('login/', views.UserLoginView.as_view(), name='user_login'),
]

urlpatterns += router.urls
