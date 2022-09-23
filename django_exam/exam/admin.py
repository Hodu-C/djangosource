from django.contrib import admin
from .models import Choice, Question
# Register your models here.

#모델을 관리하려면 모델을 불러와서 등록 설정해줘야됨
admin.site.register(Question)
admin.site.register(Choice)