from users.models import User
from users.forms import LoginForm, SignupForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def login_view(request):
  if request.method == "POST":
    user_info = {
      "username": request.POST.get("username"),
      "password": request.POST.get("password")
    }

    form = LoginForm(user_info)
    form.is_valid()
    errors = dict(form.errors)

    if len(errors) == 0:
      user = User.objects.filter(username=user_info["username"], password=user_info["password"]).first()
      if user is None:
        errors = {
          "global": ["Invalid Username or Password Entered"]
        }
        return render(request, "users/login.html", {"errors": errors, "values": user_info})

      request.session["user_id"] = user.id
    else:
      print(errors)
      return render(request, "users/login.html", {"errors": errors, "values": user_info})

  if "user_id" in request.session.keys():
    return redirect("home")

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

    form = SignupForm(user_info)
    form.is_valid()
    errors = dict(form.errors)

    if len(errors) == 0:
      if user_info["password"] != user_info["repassword"]:
        errors = {
          "repassword": ["The passwords you entered don't match"]
        }
        return render(request, "users/signup.html", {"errors": errors, "values": user_info})

      del user_info["repassword"]
      new_user = User(**user_info)
      new_user.save()
    else:
      return render(request, "users/signup.html", {"errors": errors, "values": user_info})

  if "user_id" in request.session.keys():
    return redirect("home")

  return render(request, "users/signup.html")
