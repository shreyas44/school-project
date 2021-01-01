from users.views import login_view, signup_view
from django.urls import path

urlpatterns = [
  path("login", login_view, name="login"),
  path("signup", signup_view, name="signup")
]