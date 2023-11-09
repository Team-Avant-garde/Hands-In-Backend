from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, serializers
from .models import Vote
from .serializers import VoteSerializer
from .permissions import hasSelfVotedOrReadOnly
from Post.models import Post
from rest_framework.response import Response

# Create your views here.
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, hasSelfVotedOrReadOnly]

    def perform_create(self, serializer):
        post_instance = get_object_or_404(Post, pk=self.request.data['post'])


        # If user likes the post
        if self.request.data['up_vote']:
            already_up_voted = Vote.objects.filter(post=post_instance, up_vote_by=self.request.user).exists()
        

            if already_up_voted:
                raise serializers.ValidationError({"message: You have already liked this post"})  
            else:
              serializer.save(up_vote_by=self.request.user, post=post_instance ) 

        # If dislikes
        else:
            already_down_voted = Vote.objects.filter(post=post_instance, down_vote_by=self.request.user).exists()

            if already_down_voted:
                raise serializers.ValidationError({"message: You have already disliked this post"})
            else:
              serializer.save(down_vote_by=self.request.user, post=post_instance)  

    
    def perform_update(self, serializer):
        # Get the post associated with the vote
        post_instance = get_object_or_404(Post, pk=self.request.data['post'])

        already_down_voted = Vote.objects.filter(post=post_instance, down_vote_by=self.request.user).exists()
        already_up_voted = Vote.objects.filter(post=post_instance, up_vote_by=self.request.user).exists()

        user = self.request.user
        
        # Custom logic for updating the instance
        if already_down_voted and not already_up_voted:
               vote_instance = Vote.objects.get(post=post_instance)
               vote_instance.up_vote_by = user
               vote_instance.down_vote_by = None
               vote_instance.save()
               serializer.save(up_vote_by=self.request.user, down_vote_by=None, post=post_instance)  


        if already_up_voted and not already_down_voted:
               vote_instance = Vote.objects.get(post=post_instance)
               vote_instance.up_vote_by = None
               vote_instance.down_vote_by = user
               vote_instance.save()
               serializer.save(up_vote_by=None, down_vote_by=self.request.user, post=post_instance)  
             