from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProfileForm
# Create your views here.
def add_profile(request):
    if request.method == "POST":
        add_profile_from = ProfileForm(request.POST)
        if add_profile_from.is_valid():
            add_profile_from.save()
            return redirect("add_profile")
    else:
        add_profile_from = ProfileForm()
    context = {
        "form": add_profile_from
    }
    return render(request, "add_post.html", context)
