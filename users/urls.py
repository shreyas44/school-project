from users.views import login_view, logout_view, signup_view
from django.urls import path

urlpatterns = [
  path("login", login_view, name="login"),
  path("signup", signup_view, name="signup"),
  path("logout", logout_view, name="logout")
]