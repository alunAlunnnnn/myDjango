from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


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













