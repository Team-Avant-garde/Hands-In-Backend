from .models import Request
from rest_framework import serializers


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('id', 'user', 'post', 'give_hand')