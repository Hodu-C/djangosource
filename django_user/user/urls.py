from django.urls import path
from django.contrib.auth.urls import views
from . import views

app_name = "user"

urlpatterns = [
    # http://127.0.0.1:8000/user/
    path("", views.index,name="index"),

    #  http://127.0.0.1:8000/user/signup/
    path("signup/", views.signup,name="signup"),

    #  http://127.0.0.1:8000/user/login/
    # path("login/", views.custom_login,name="login"),
    
    # path("logout/", views.custom_logout, name="logout"),
    
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"),name="login"),
    path("logout/", auth_views.LogoutView.as_view(),name="logout"),
    
    # http://127.0.0.1:8000/user/password_chage/
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="user/password_change.html"),name="password_chage")
]
