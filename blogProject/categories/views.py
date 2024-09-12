from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CategoryForm
# Create your views here.
def add_catagory(request):
    if request.method == "POST":
        add_category_form = CategoryForm(request.POST)
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect("add_catagory")
    else:
        add_category_form = CategoryForm()
    context = {
        "form": add_category_form
    }
    return render(request, "add_category.html", context)