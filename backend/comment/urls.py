from django.urls import path, include
from .views import CommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comment', CommentViewSet)

urlpatterns = router.urls     