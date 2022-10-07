from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Question, Answer, Comment


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("subject", "created_at")
    search_fields = ["subject"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
