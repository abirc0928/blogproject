from django.urls import path, include
from .import views

urlpatterns = [
    path('singin/', views.signin, name='sign_in'),
    path('singup/', views.registration, name='registration'),
    path('logout/', views.logout_view, name='logout'),
]