from django.db import models


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=32)


class Student(models.Model):
    name = models.CharField(max_length=32)

    # 添加外键，此处会自动匹配到 Class 模型的 id 字段
    fk_student_grade_id = models.ForeignKey(Class)
