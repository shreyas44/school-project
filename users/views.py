from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def login_view(request):
  if request.method == "POST":
    user_info = {
      "username": request.POST.get("username"),
      "password": request.POST.get("password")
    }
    print(user_info)
  return render(request, "users/login.html")

def signup_view(request):
  if request.method == "POST":
    user_info = {
      "first_name": request.POST.get("firstname"),
      "last_name": request.POST.get("lastname"),
      "username": request.POST.get("username"),
      "password": request.POST.get("password"),
      "repassword": request.POST.get("repassword"),
    }

    print(user_info)
  return render(request, "users/signup.html")
