from django.urls import path
from . import views


app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.question_detail, name="question_detail"),
    path("question/create/", views.question_create, name="question_create"),
    
    path("answer/create/<int:question_id>/", views.answer_create, name="answer_create"),
]