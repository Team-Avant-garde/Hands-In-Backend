from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def home(request):
    html_content = """
    <!DOCTYPE html>
<html>
<head>
<title>Handsin | API Routes</title>
<style>
html {
background-color: #C8C8C8;
color: black;
}
a {
text-decoration: none;
color: black;
font-weight: bold;

}

table {
  border-collapse: collapse;
  width: 100%;
    border-color: black;
    border-width: 1px;

}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {background-color: #f2f2f2;}
</style>
</head>
<body>

<h2 style="text-align: center; font-weight: bold">Hello, Welcome to Hands-In Api</h2>

<div style="overflow-x: auto;">
  <table>
    <tr>
      <th>Title</th>
      <th>URL</th>
      <th>Type</th>
      <th>Route</th>
    </tr>
    <tr>
      <td>Sign Up</td>
      <td><a href="http://handsin.onrender.com/api/auth/signup">Link</a></td>
      <td>POST</td>
      <td>/api/auth/user/</td>
      
    </tr>
    <tr>
      <td>User Login</td>
      <td><a href="https://handsin.onrender.com/api/auth/login/">Link</a></td>
      <td>GET</td>
      <td>/api/auth/login/</td>
    </tr>
    <tr>
      <td>Admin</td>
      <td><a href="https://handsin.onrender.com/admin/">Link</a></td>
      <td>None</td>
      <td>/admin/</td>
    </tr>
    <tr>
      <td>Comment</td>
      <td><a href="https://handsin.onrender.com/api/comments/comment/">Link</a></td>
      <td>POST</td>
      <td>/api/comments/comment/</td>
    </tr>
    <tr>
      <td>Vote</td>
      <td><a href="https://handsin.onrender.com/api/votes/vote/">Link</a></td>
      <td>POST</td>
      <td>/api/votes/vote/</td>
    </tr>
    <tr>
      <td>Post</td>
      <td><a href="https://handsin.onrender.com/api/votes/vote/">Link</a></td>
      <td>POST</td>
      <td>/api/votes/vote/</td>
    </tr>
  </table>
</div>

</body>
</html>
    """
    return HttpResponse(html_content)
