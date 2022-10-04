from django.db import models
from user.models import User

from taggit.managers import TaggableManager

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
    
    #좋아요 - 다대다 연결
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    
    # tag
    tags = TaggableManager(blank=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Comment(models.Model):
    """
    글번호(PK), 내용, 작성날짜, 수정날짜, 작성자
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return "%s - %s" %(self.id, self.user)
    

    