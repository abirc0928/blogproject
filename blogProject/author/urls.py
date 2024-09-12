from django.urls import path, include
from .import views

urlpatterns = [
    path('add_author/', views.add_author, name='add_author'),
]