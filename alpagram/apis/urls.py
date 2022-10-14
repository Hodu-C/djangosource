from django.urls import path
from . import views

urlpatterns = [
    # User 생성
    path("v1/users/create/",
         views.UserCreateView.as_view(),
         name="apis_v1_users_create"),
]
