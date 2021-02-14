from django.conf.urls import url
from App import views

urlpatterns = [
    # 添加一个新的路由
    url(r'^index_app/', views.index_app),

    # 添加template的路由
    url(r'^return_html/', views.return_html),

    url(r'^template_str/', views.template_str),

    # 模型添加记录
    url(r'^add/', views.add),

    # 模型查询
    url(r'^selectOne/', views.selectOne),

    url(r'^selectAll/', views.selectAll),

    # 删除
    url(r'^delete/', views.delete),

    # 修改
    url(r'^modify/', views.modify)

]
