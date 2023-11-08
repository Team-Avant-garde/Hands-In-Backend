from rest_framework import serializers
from .models import Post
from comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'tag', 'owner', 'post_image', 'post_date', 'is_solved', 'updated_at', 'comments')