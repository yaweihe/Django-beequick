# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import Wheel,Nav
from django.http import  JsonResponse

from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User,Cart,Order
from .forms.login import LoginForm
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import logout
import time,random,os
# Create your views here.
def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()

    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]

    mainList = MainShow.objects.all()
    return render(request,'beequick/home.html',{"title":"主页" ,"wheelsList":wheelsList, "navList":navList,"mustbuyList":mustbuyList,"shop1":shop1,
                                                "shop2": shop2,"shop3":shop3,"shop4":shop4, "mainList": mainList})

def market(request,categoryid,cid,sortid):
    leftSlider = FoodTypes.objects.all()
    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        productList = Goods.objects.filter(categoryid=categoryid,childcid = cid)

    #排序
    #按销量排序 productnum
    if sortid == '1':
       productList = productList.order_by("productnum")
    #按价格最低排序
    elif sortid == '2':
        productList = productList.order_by("price")
    #按价格最高排序
    elif sortid == '3':
        productList = productList.order_by("price")[::-1]

    childList = []
    group = FoodTypes.objects.get(typeid = categoryid)
    #print(categoryid)
    childnames = group.childtypenames
    #print (childnames)
    #全部分类：0#进口水果:103534#国产水果:103533
    arr1 = childnames.split('#')
    for str in arr1:
        ##全部分类：0
        arr2 = str.split(":")
        obj = {"childName":arr2[0],"childId":arr2[1]}
        childList.append(obj)

    #titlelist = [{"title": "综合排序", "index": "0"}, {"title": "销量排序", "index": "1"}, {"title": "价格最低", "index": "2"},{"title": "价格最高", "index": "3"}]
    #print (titlelist)

    #获取所登录用户，在闪送超市中选购到商品的数量
    token = request.session.get("token")
    cartList = []
    if token:
        user = User.objects.get(userToken=token)
        cartList = Cart.objects.filter(userAccount = user.userAccount)

    for p in productList:
        for c in cartList:
            if c.productid == p.productid:
                p.num = c.productnum
                continue

    return render(request,'beequick/market.html',{"title":"闪送超市" ,"leftSlider":leftSlider,"productList":productList,"childList":childList,"categoryid":categoryid,"cid":cid,"cartList":cartList})

def cart(request):
    cartList = []
    token = request.session.get("token")
    if token != None:
        user = User.objects.get(userToken = token)
        cartList = Cart.objects.filter(userAccount = user.userAccount)

    return render(request,'beequick/cart.html',{"title":"购物车","cartList":cartList })

#修改购物车
def changecart(request,flag):
    #判断用户是否登录
    token = request.session.get("token")
    if token == None:
        # 没登录
        # 注： ajax 下重定向是不行的
        # -1 表示未登录
        return JsonResponse({"data":"-1","status":"error"})

    productid = request.POST.get("productid")
    product = Goods.objects.get(productid=productid)
    user = User.objects.get(userToken = token)
    #添加
    if flag == '0':
        if product.storenums == 0:
            return JsonResponse({"data":-2,"status":"error"})
        #用户的所有订单
        carts = Cart.objects.filter(userAccount = user.userAccount)
        onecart = None
        if carts.count == 0:
            #直接增加一条
            onecart = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
            onecart.save()
        else:
            try:
                onecart = carts.get(productid = productid)
                #修改数量和价格
                onecart.productnum += 1
                onecart.productprice ="%.2f" %(onecart.productnum * product.price)
                onecart.save()
            except Cart.DoesNotExist as e:
                #如果没拿到该商品，直接增加一条
                onecart = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,
                                    product.productlongname, False)
                onecart.save()

        #库存减一
        product.storenums -= 1
        product.save()
        return JsonResponse({"data":onecart.productnum,"price":onecart.productprice,"status":"success"})
    #减少
    elif flag == '1':
        carts = Cart.objects.filter(userAccount = user.userAccount)
        onecart = None
        if carts.count() == 0:
            return JsonResponse({"data": -2, "status": "error"})
        else:
            try:
                onecart = carts.get(productid=productid)
                # 修改数量和价格
                onecart.productnum -= 1
                onecart.productprice = "%.2f" % (product.price * onecart.productnum)
                if onecart.productnum == 0:
                    onecart.delete()
                else:
                    onecart.save()
            except Cart.DoesNotExist as e:
                return JsonResponse({"data": -2, "status": "error"})
            # 库存加1
        product.storenums += 1
        product.save()
        return JsonResponse({"data": onecart.productnum,"price":onecart.productprice, "status": "success"})
    #在购物车中取消勾选项
    elif flag == '2':
        carts = Cart.objects.filter(userAccount = user.userAccount)
        onecart = carts.get(productid = productid)
        onecart.isChose = not onecart.isChose
        onecart.save()
        str = ""
        if onecart.isChose:
            str = "√"
        return JsonResponse({"data":str,"status":"success"})

    elif flag == '3':
        pass




def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息格式没问题，验证账号和密码的正确性
            print("*******")
            name = f.cleaned_data["username"]
            pswd = f.cleaned_data["password"]
            try:
                user = User.objects.get(userAccount = name)
                if user.userPasswd != pswd:
                    return redirect('/login/')
            except User.DoesNotExist as e:
                return redirect('/login/')

            #登录成功
            token = time.time() + random.randrange(1,100000)
            user.userToken = str(token)
            user.save()
            request.session["username"] = user.userName
            request.session["token"] = user.userToken
            return redirect('/mine/')
        else:
            return render(request, 'beequick/login.html', {"title": "登录","forms":f,"error":f.errors})
    else:
        f = LoginForm()
        return render(request, 'beequick/login.html', {"title": "登录","forms":f})

def saveorder(request):
    token = request.session.get("token")
    if token == None:
        return JsonResponse({"data":-1,"status":"error"})
    user = User.objects.get(userToken = token)
    carts = Cart.objects.filter(isChose=True)
    if carts.count() == 0:
        return JsonResponse({"data":-1, "status":"error"})
    oid = time.time() + random.randrange(1,100000)
    oid = "%d"%oid
    order = Order.creatorder(oid,user.userAccount,0)
    order.save()
    for item in carts:
        item.isDelete = True
        item.orderid = oid
        item.save()
    return JsonResponse({"status":"success"})



def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        #userImg = request.POST.get("userImg")
        userRank = 0
        userToken = str(time.time() + random.randrange(1,1000000))
        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MEDIA_ROOT,userAccount+".png")

        with open (userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)
        user = User.createuser(userAccount,userPasswd,userName,userPhone,userAddress,userImg,userRank,userToken)
        user.save()

        request.session["username"] = userName
        request.session["token"] = userToken
        return redirect('/mine/')
    else:
        return render(request,'beequick/register.html',{"title":"注册"})
def checkuserid(request):
    #判断用户是否登录
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount = userid)
        return JsonResponse({"data":"该用户已经被注册","status":"error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"可以注册","status":"success"})

def quit(request):
    logout(request)
    return redirect('/mine/')

def mine(request):
    username = request.session.get("username","未登录")
    return render(request,'beequick/mine.html',{"title":"我的","username":username})