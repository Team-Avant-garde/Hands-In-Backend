from django.db import models
from Post.models import Post
from Account.models import User

# Create your models here.
class CommentView(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=4000)
    comment_image = models.CharField(max_length=255, null=True, blank=True)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment