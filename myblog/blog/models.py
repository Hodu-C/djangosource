from django.db import models
from user.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    
    # auto_now_add : 처음 생성됐을 때를 확인
    # auto_now - 수정일자 수정 될때마다 갱신
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title