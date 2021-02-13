"""MyDjangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from MyDjangoProject import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 添加一个新的路由
    url(r'^index/', views.index),

    # 引用 App 中的子路由
    url(r'^app/', include('App.urls')),

    # 引用 viewreturn 中的子路由
    url(r'^viewreturn/', include('viewreturn.urls')),
]
