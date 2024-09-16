from django.contrib import admin
from django.urls import path, include
from .viwes import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="homepage"), #home
    path('author/', include('author.urls')), # Author Page URL
    path('profile/', include('profiles.urls')), # Profile Page URL
    path('post/', include('posts.urls')), # Categories Page URL
    path('category/', include('categories.urls')), # Posts Page URL
    path('authentication/', include('authentication.urls')), # Posts Page URL
]
