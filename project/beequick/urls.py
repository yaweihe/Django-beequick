# coding=utf-8
from django.conf.urls import url

from . import  views
urlpatterns = [
    # 主页
    url(r'^$', views.home),
    url(r'^home/$', views.home, name='home'),
    #闪送超市
    url(r'^market/(\d+)/(\d+)/(\d+)/$',views.market, name='market'),
    #购物车
    url(r'^cart/$',views.cart, name='cart'),
    #修改购物车
    url(r'^changecart/(\d+)/$',views.changecart,name="changecart"),
    #下订单
    url(r'^saveorder/$',views.saveorder,name="saveorder"),

    #我的
    url(r'^mine/$',views.mine, name= 'mine'),
    #登录
    url(r'^login/$',views.login,name='login'),
    #注册
    url(r'^register/$',views.register,name='register'),
    #验证账号是否被注册
    url(r'^checkuserid/$',views.checkuserid,name='checkuserid'),
    #退出登录
    url(r'^quit/$',views.quit,name='quit'),
]
