from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import Post

# Create your views here.
def add_post(request):
    if request.method == "POST":
        add_post_from = PostForm(request.POST)
        if add_post_from.is_valid():
            add_post_from.save()
            return redirect("homepage")
    else:
        add_post_from = PostForm()
    context = {
        "form": add_post_from
    }
    return render(request, "add_post.html", context)


def delete_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.delete()
    except post.DoesNotExist:
        return HttpResponse("Task does not exist")
    return redirect("homepage")


def update_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
        if request.method == "POST":
            post_form = PostForm(request.POST, instance = post)
            if post_form.is_valid():
                post_form.save()
                return redirect("homepage")
            else:
                return render(request, "update_post.html", {"form": post_form})

        post_form = PostForm(instance=post)
        return render(request, "update_post.html", {"form": post_form})

    except Post.DoesNotExist:
        return HttpResponse("Task does not exist")

def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context= {
        "post": post
    }
    return render(request, "single_post.html",context)