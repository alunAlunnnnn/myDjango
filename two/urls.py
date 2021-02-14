from django.conf.urls import url

from two import views

urlpatterns = [
    # 向班级表中插入数据
    url(r'^inDataClass/', views.inDataClass),

    # 向学生表中插入数据
    url(r'^inDataStudent/', views.inDataStudent),

    # 一对多查询
    url(r'^queryFromClass/', views.queryFromClass),

    url(r'^queryFromStudent/', views.queryFromStudent),
]
