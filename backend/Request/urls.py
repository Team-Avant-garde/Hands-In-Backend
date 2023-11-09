from django.urls import path
from . views import RequestView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'request', RequestView)

urlpatterns = [
    
]
urlpatterns += router.urls