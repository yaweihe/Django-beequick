# Django-beequick
Django爱鲜蜂商城项目根据千峰网课教程编写，除了复现代码之外，做了一定的优化，旨在熟悉与理解Django框架。


# 在本地运行项目
克隆项目到本地
  git clone https://github.com/yaweihe/Django-beequick
  
安装环境
  
迁移数据库
  在下一行代码运行前，请根据你的数据库实际情况，修改项目文件夹beequick下settings.py文件中的DATABASES配置（本例采用的是MySQL数据库，并用PyMysql进行管理）
  python manage.py migrate
  
创建后台管理员账户
python manage.py createsuperuser

运行服务器
python manage.py runserver

添加商品分类及相应分类对应的商品
在浏览器输入：127.0.0.1:8000/admin，登录到后台,

项目预览
在浏览器输入：127.0.0.1:8000，查看效果。
