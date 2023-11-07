from django.urls import path, include


urlpatterns = [
    path('post/', include('Post.urls')),
    path('auth/', include('Account.urls')),
]
