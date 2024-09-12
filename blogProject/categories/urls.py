from django.urls import path, include
from .import views

urlpatterns = [
    path('add_catagory/', views.add_catagory, name='add_catagory'),
]