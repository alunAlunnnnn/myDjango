from django.db import models


# Create your models here.

class Animal(models.Model):
    # 创建字符串字段
    name = models.CharField(max_length=32)
    # 创建整型字段
    age = models.IntegerField()

    type = models.CharField(max_length=32, default='未知')
