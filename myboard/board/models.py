from django.db import models

# Create your models here.
#질문 모델(Question)
#제목(Subject-200자), 내용(content - TextField), create_at(작성일시 - DatetimeField)
class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜")
    
    def __str__(self) -> str:
        return self.subject

#답변 모델(Answer)
# - 질문 - 답변(comment) 관게모델 질문ID <-> 답변ID (일 대 다 관계)
#내용(content), crate_at

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
    content = models.TextField(verbose_name="내용")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성 날짜")