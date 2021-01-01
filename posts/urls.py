from posts.views import home_view, new_post, toggle_like
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
  path("home", home_view, name="home"),
  path("toggleLike", csrf_exempt(toggle_like), name="toggle_like"),
  path("newPost", csrf_exempt(new_post), name="new_post")
]