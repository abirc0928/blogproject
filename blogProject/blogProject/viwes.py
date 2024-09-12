from django.shortcuts import render
from posts.models import Post
from .forms import SearchForm

# Create your views here.
def home(request):
    query = request.GET.get('query', None)
    posts = Post.objects.all()

    # Filter posts based on the search query
    if query:
        posts = posts.filter(title__icontains=query) | posts.filter(content__icontains=query)

    context = {
        "posts": posts,
        "SearchForm": SearchForm(),
    }
    return render(request, "home.html", context)



# def search_form(request):
#     return {'SearchForm': SearchForm()}

