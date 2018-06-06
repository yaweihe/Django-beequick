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

