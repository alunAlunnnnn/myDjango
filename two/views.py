from django.shortcuts import render
from django.http import HttpResponse
from two.models import Grade, Student
from faker import Faker


# Create your views here.

def inDataClass(request):
    names = ['一班', '二班', '三班', '四班']
    for i, name in enumerate(names):
        i += 1
        oClass = Grade()
        # oClass.id = i
        oClass.name = name
        oClass.save()

    return HttpResponse('插入成功')


def inDataStudent(request):
    f = Faker(locale="zh_CN")

    num = 0
    # 四个班级
    for i in range(1, 5):
        print(i)
        # 每个班级15个人
        for j in range(15):
            print(j)
            num += 1
            oStudent = Student()
            oStudent.id = num
            oStudent.name = f.name()
            oStudent.fk_student_grade_id = i
            oStudent.save()

    return HttpResponse('插入成功')


def queryFromClass(request):
    # 首先查询主表
    oClass = Grade.objects.get(pk=2)
    print(oClass.student_set)
    studentList = oClass.student_set

    return HttpResponse(f'查询成功 {oClass.id, oClass.name} {studentList}')


def queryFromStudent(request):
    oStudent = Student.objects.get(pk=3)
    name = oStudent.s_grade.name
    print(name)

    return HttpResponse(f'ok {name} {oStudent.name}')