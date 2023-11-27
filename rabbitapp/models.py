from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):
    title = models.CharField(verbose_name='カテゴリ',max_length=20)

    def __str__(self):
        return self.title

class RabbitPost(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE) # ユーザーを削除する同時に存在する写真も削除する
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT) # カテゴリを削除できなくなる
    title = models.CharField(verbose_name='アイテム', max_length=200)
    comment = models.TextField(verbose_name='コメント')
    image1 = models.ImageField(verbose_name='イメージ1', upload_to='photos')
    image2 = models.ImageField(verbose_name='イメージ2', upload_to='photos', blank=True, null=True)
    qty = models.IntegerField(verbose_name='数量')
    posted_at = models.DateTimeField(verbose_name='更新日', auto_now_add=True)
    price = models.IntegerField(verbose_name='値段')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='購入アイテム')
    price = models.IntegerField(verbose_name='単価')
    qty = models.IntegerField(verbose_name='購入数量')

    def __str__(self):
        return self.title

class Record(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='購入したアイテム')
    price = models.IntegerField(verbose_name='購入する時の単価')
    qty = models.IntegerField(verbose_name='購入した数量')
    buying_date = models.DateField(verbose_name='購入日', auto_now_add=True)

    def __str__(self):
        return self.title