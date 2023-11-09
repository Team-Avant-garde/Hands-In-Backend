from django.db import models
from Account.models import User
from Post.models import Post

# Create your models here.
class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    give_hand = models.BooleanField(default=False)


def __str__(self):
    return self.user.username