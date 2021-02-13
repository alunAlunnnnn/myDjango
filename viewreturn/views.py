from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def return_str(request):
    return HttpResponse('return string')


def return_html(request):
    return render(request, "testRender.html")