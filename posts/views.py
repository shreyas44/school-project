from django.db.models.aggregates import Count
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from datetime import datetime 
import time
import json
from users.models import User
from .models import Like, Post

def home_view(request):
  if "user_id" not in request.session.keys():
    return redirect("login")

  user = User.objects.get(id=request.session["user_id"])
  posts = Post.objects.all().annotate(likes_count=Count("likes")).order_by("-timestamp").select_related()

  formatted_posts = []

  for post in posts:
    formatted_timestamp = datetime.utcfromtimestamp(post.timestamp).strftime('%-d %b %y')
    formatted_post = post
    formatted_post.timestamp = formatted_timestamp

    is_liked = True
    like = Like.objects.filter(user=user, post=post).first()
    if like is None:
      is_liked = False

    formatted_post.is_liked = is_liked
    formatted_posts.append(formatted_post)

  data = {
    "posts": formatted_posts,
    "user": user,
  }

  return render(request, "posts/home.html", data)

def toggle_like(request):
  if request.method == "POST":
    user_id = request.session["user_id"]
    user = User.objects.get(id=user_id)
    body = json.loads(request.body)

    like = Like.objects.filter(user=user, post_id=body["post_id"]).first()

    if like is None:
      new_like = Like(user=user, post_id=body["post_id"], timestamp=time.time())
      new_like.save()
      response = "increase"
    else:
      response = "decrease"
      like.delete()

    return HttpResponse(response)

  return HttpResponseForbidden()
