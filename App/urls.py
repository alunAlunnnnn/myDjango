from django.conf.urls import url
from App import views

urlpatterns = [
    # 添加一个新的路由
    url(r'^index_app/', views.index_app),

    # 添加template的路由
    url(r'^return_html/', views.return_html),
]
