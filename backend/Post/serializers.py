from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tag', 'owner', 'post_image', 'post_date', 'is_solved', 'updated_at')