from users.views import login_view, signup_view
from django.urls import path

urlpatterns = [
  path("login", login_view),
  path("signup", signup_view)
]