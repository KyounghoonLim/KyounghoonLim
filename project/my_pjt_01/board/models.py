from django.db import models

# Create your models here.
class Board(models.Model):
    head_form = [
        ('', '말머리를 선택해주세요'),
        ('1', '자유게시판'),
        ('2', '강의 다시보기'),
    ]
    header = models.TextField(choices=head_form)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    image = models.ImageField(blank=True, upload_to='assets/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cnt = models.IntegerField(default=0)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
