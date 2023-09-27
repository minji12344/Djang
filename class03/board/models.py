from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20) # 글자 수
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 글을 등록할 때마다 시간

    def __str__(self):
        return self.title
    