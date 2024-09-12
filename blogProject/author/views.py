from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AuthorForm
# Create your views here.
def add_author(request):
    if request.method == "POST":
        add_author_from = AuthorForm(request.POST)
        if add_author_from.is_valid():
            add_author_from.save()
            print(add_author_from)
            return redirect("add_author")
    else:
        add_author_from = AuthorForm()
    context = {
        "form": add_author_from
    }
    return render(request, "add_author.html", context)
   