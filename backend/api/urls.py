from django.urls import path, include

from . import views


urlpatterns = [
    path("", view=views.home, name="api-home"),
    path("post/", include("Post.urls")),
    path("auth/", include("Account.urls")),
]
