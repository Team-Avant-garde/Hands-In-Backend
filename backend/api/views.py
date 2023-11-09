from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def home(request):
    return Response(
        {"message: Welcome to the Hands-In API!", 
        "SignUp: /api/auth/user/",
        "LogIn: /api/auth/login/",
        "Post: /api/posts/post/",
        "comment: /api/comments/comment/",
        "Votes: /api/votes/vote/"},
        status=status.HTTP_200_OK
    )

