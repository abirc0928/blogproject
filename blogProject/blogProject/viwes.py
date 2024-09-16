from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from .forms import SearchForm

# Create your views here.
def home(request):
    query = request.GET.get('query', None)
    posts = Post.objects.all()
    user_email =  request.session.get('email')
    user_name =  request.session.get('username')
    # Filter posts based on the search query
    if query:
        posts = posts.filter(title__icontains=query) | \
                posts.filter(content__icontains=query) | \
                posts.filter(author__name__icontains=query)
                
        print("posts: ",posts)

    context = {
        "posts": posts,
        "SearchForm": SearchForm(),
        "user_email": user_email,
        "user_name": user_name
    }
    return render(request, "home.html", context)



