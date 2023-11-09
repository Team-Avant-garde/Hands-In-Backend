from django.db import models
from Post.models import Post
from Account.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=4000)
    comment_image = CloudinaryField(blank=True)
    comment_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Comment, self).save(*args, **kwargs)

        # Check if a comment has been made on the post
        if self.post:
            # Set the is_solved variable of the associated Post to True
            self.post.is_solved = True
            self.post.save()







    def __str__(self):
        return self.comment
    