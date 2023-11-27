from django.db import models

# Create your models here.

class PyTest(models.Model):
    title = models.CharField(max_length=200, verbose_name='問題')
    ans = models.TextField(max_length=500, verbose_name='答え')
    content = models.TextField(max_length=500, verbose_name='内容')

    def __str__(self):
        return self.title