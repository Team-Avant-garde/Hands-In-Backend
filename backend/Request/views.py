from django.shortcuts import render
from rest_framework import viewsets
from . models import Request
from . serializers import RequestSerializer

# Create your views here.
class RequestView(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer