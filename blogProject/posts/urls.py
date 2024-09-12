from django.urls import path, include
from .import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post"), # Delete posts
    path('update_post/<int:post_id>', views.update_post, name="update_post"), # update posts
]