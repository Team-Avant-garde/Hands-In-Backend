from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    content = models.CharField(max_length=4000)
    tag = models.CharField(max_length=50, db_index=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    is_solved = models.BooleanField(default=False)
    post_image = models.CharField(max_length=255, blank=True)
    post_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title