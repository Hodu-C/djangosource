from django.urls import path
from . import views


urlpatterns = [
    #http://127.0.0.1:8000/user_register/
    path("register/", views.user_register, name="user_register"),
    
]
