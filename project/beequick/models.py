# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#
class Wheel(models.Model):
    img  = models.CharField(max_length=150)
    name = models.CharField(max_length=25)
    trackid = models.CharField(max_length=10)
    isDelete = models.BooleanField(default=False)
#轮播图模型
class Nav(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=20)
#每日必抢模型
class Mustbuy(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=20)
#便利店数据模型
class Shop(models.Model):
    img = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    trackid = models.CharField(max_length=20)
#主要展示
class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()
#分类模型
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)
#商品模型类
class Goods(models.Model):
    #商品id
    productid = models.CharField(max_length=10)
    #商品图片
    productimg = models.CharField(max_length=150)
    #商品名称
    productname = models.CharField(max_length=50)
    #商品长名称
    productlongname = models.CharField(max_length=100)
    #是否精选
    isxf = models.NullBooleanField(default=False)
    #是否买一赠一
    pmdesc = models.CharField(max_length=10)
    #规格
    specifics = models.CharField(max_length=20)
    #价格
    price = models.FloatField()
    #超市价格
    marketprice = models.FloatField()
    #组id
    categoryid = models.CharField(max_length=10)
    #子组id
    childcid = models.CharField(max_length=10)
    #子类组名称
    childcidname = models.CharField(max_length=10)
    #详情页
    dealerid = models.CharField(max_length=10)
    #库存
    storenums = models.IntegerField()
    #销量
    productnum = models.IntegerField()
    #是否删除
    isDelete = models.NullBooleanField(default=False)

# 用户模型类
class User(models.Model):
    # 用户账号，要唯一
    userAccount = models.CharField(max_length=20,unique=True)
    # 密码
    userPasswd  = models.CharField(max_length=20)
    # 昵称
    userName    =  models.CharField(max_length=20)
    # 手机号
    userPhone   = models.CharField(max_length=20)
    # 地址
    userAdderss = models.CharField(max_length=100)
    # 头像路径
    userImg     = models.CharField(max_length=150)
    # 等级
    userRank    = models.IntegerField()
    # touken验证值，每次登陆之后都会更新
    userToken   = models.CharField(max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u
#设置objects过滤条件，isDelete=False的不显示
class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1,self).get_queryset().filter(isDelete=False)
#购物车模型类
class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.FloatField()
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20,default="0")
    isDelete = models.BooleanField(default=False)
    #自定义模型管理器
    #
    objects = CartManager1()
    #查看订单
    #object2 = CartManager2()
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount = userAccount,productid = productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c

class Order(models.Model):
    orderid = models.CharField(max_length=20)
    userid = models.CharField(max_length=20)
    progress = models.IntegerField()
    @classmethod
    def creatorder(cls, orderid, userid, progress):
        order = cls(orderid=orderid, userid=userid, progress=progress)
        return order