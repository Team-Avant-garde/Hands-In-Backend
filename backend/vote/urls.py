from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import VoteViewSet

router = DefaultRouter()
router.register(r'vote', VoteViewSet)

urlpatterns = router.urls