# coding=utf-8
from django.conf.urls import url

from . import  views
urlpatterns = [
    # 主页
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),

    url(r'^market/$',views.market, name='market'),
    url(r'^cart/$',views.cart, name='cart'),
    url(r'^mine/$',views.mine, name= 'mine'),
]
