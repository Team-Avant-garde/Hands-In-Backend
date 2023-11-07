from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
<<<<<<< HEAD
from rest_framework.decorators import api_view

# Create your views here.

=======

# Create your views here.
>>>>>>> 13eb608 (Add post models and serializers)
class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)