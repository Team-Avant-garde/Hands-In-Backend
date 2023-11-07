from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset

router = DefaultRouter()
router.register(r'post', PostViewset)


urlpatterns = [
<<<<<<< HEAD
    path('', include(router.urls)),
=======
    path(router.urls),
>>>>>>> 13eb608 (Add post models and serializers)
]
