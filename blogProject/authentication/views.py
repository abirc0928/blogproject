from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name"]

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            request.session['email'] = user.email
            request.session['username'] = user.username
            return redirect("homepage")
    else:
        form = AuthenticationForm()
    context = {
        "form": form
    }
    
    return render(request, "signin.html", context)

def registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("registration")
    else:
        form = CustomUserCreationForm()
    context = {
        "form" : form
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect("homepage")

