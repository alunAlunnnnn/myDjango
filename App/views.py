from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index_app(request):
    return HttpResponse("index_app")


def return_html(request):
    return render(request, 'testRender.html')