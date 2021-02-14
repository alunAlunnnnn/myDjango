from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from App.models import Animal


def index_app(request):
    return HttpResponse("index_app")


def return_html(request):
    context = {
        'name': '张三'
    }

    return render(request, 'testRender.html', context=context)


def template_str(request):
    scores = [i * 10 for i in range(1, 11)]

    context = {
        'scores': scores
    }

    return render(request, 'templateStr.html', context=context)


def add(request):
    # 实例化模型
    animal = Animal()

    # 属性赋值
    animal.name = '噗噗'
    animal.age = 1
    animal.type = '狗子'

    # 保存记录
    animal.save()

    return HttpResponse("添加成功")


def selectOne(request):
    # 查询一个
    # res = Animal.objects.get(pk=1)
    res = Animal.objects.get()

    print(res.name, res.age, res.type)

    return HttpResponse(f'查询成功 --- {res.name}, {res.age}, {res.type}')


def selectAll(request):
    # 查询所有
    res_list = Animal.objects.all()
    resStr = ''
    for res in res_list:
        resStr = resStr + str(res.name) + ' ' + \
                 str(res.age) + ' ' + str(res.type) + '\n'
    print(resStr)

    return HttpResponse(f'查询成功 --- {resStr}')


def delete(request):
    # 先查询，再调用查询对象的 .delete() 方法
    res = Animal.objects.get(pk=1)
    res.delete()

    return HttpResponse(f'删除 —— {res.name, res.age, res.type}, 成功')


def modify(request):
    res = Animal.objects.get(pk=2)
    res.id = 1
    res.name = 'lucky'
    res.age = '2'
    res.type = '博美'
    res.save()

    return HttpResponse(f'修改成功 -- 修改为 {res.name, res.age, res.type}')