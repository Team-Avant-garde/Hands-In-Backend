from django.contrib import admin
from .models import Vote

# Register your models here.

class AdminVote(admin.ModelAdmin):

    list_display = ["id", "post", "up_vote_by", "down_vote_by"]
    



admin.site.register(Vote, AdminVote)