from django.urls import path, include

from . import views


urlpatterns = [
    path("", view=views.home, name="api-home"),
    path("posts/", include("Post.urls")),
    path("auth/", include("Account.urls")),
    path("comments/", include("comment.urls")),
    path("votes/", include("vote.urls")),
    path("requests/", include("Request.urls")),
]
