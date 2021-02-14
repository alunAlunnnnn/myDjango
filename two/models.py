from django.db import models


# Create your models here.

class Grade(models.Model):
    name = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)

    # 添加外键，此处会自动匹配到 Class 模型的 id 字段
    s_grade = models.ForeignKey('Grade')


class Cat(models.Model):
    name = models.CharField(max_length=32)

    # 定义源信息
    class Meta:
        db_table = 'cat'
