from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100)

class SignupForm(forms.Form):
  first_name = forms.CharField(max_length=100)
  last_name = forms.CharField(max_length=100)
  username = forms.CharField(max_length=100)
  password = forms.CharField(max_length=100)