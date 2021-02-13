from django.conf.urls import url
from viewreturn import views

urlpatterns = [
    url(r'^return_str/', views.return_str),

    url(r'^return_html/', views.return_html),
]
