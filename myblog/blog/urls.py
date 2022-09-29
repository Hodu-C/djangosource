from django.urls import path
from . import views


urlpatterns = [
    #http://127.0.0.1:8000/blog/post/
    path("post/", views.posts_list, name='post_list'),
    
    #http://127.0.0.1:8000/blog/post_write/
    path("post/write/", views.posts_write, name='post_write'),
]
