from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
