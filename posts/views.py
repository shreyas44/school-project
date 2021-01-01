from django.shortcuts import redirect, render
from datetime import datetime
from users.models import User
from .models import Post

def home_view(request):
  if "user_id" not in request.session.keys():
    return redirect("login")

  user = User.objects.get(id=request.session["user_id"])
  posts = Post.objects.all().order_by("-timestamp").select_related()
  print(posts)

  formatted_posts = []

  for post in posts:
    formatted_timestamp = datetime.utcfromtimestamp(post.timestamp).strftime('%-d %b %y')
    formatted_post = post
    formatted_post.timestamp = formatted_timestamp
    formatted_posts.append(formatted_post)

  data = {
    "posts": formatted_posts,
    "user": user,
  }

  return render(request, "posts/home.html", data)