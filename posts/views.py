from django.shortcuts import redirect, render
from users.models import User

def home_view(request):
  if "user_id" in request.session.keys():
    return redirect("login")

  user = User.objects.get(id=request.session["user_id"])

  return render(request, "posts/home.html")