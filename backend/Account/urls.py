from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", views.UserSignupView, basename="user")


urlpatterns = [ 
    
]

urlpatterns += router.urls
