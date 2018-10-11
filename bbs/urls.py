"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include #include需要导入才能使用二级路由
from django.contrib import admin
from blog import views
from django.views.static import serve #配置media用，固定写法
from django.conf import settings #配置media用，固定写法
from blog import urls as blog_urls #二级路由

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.login),
    url(r'^logout/',views.logout),
    url(r'^reg/', views.register),
    url(r'^index/', views.index),
    #将所有以blog开头的url都交给app下面的urls.py来处理
    url(r'^blog/', include(blog_urls)),
    url(r'^get_valid_img.png/', views.get_valid_img),
    # 极验滑动验证码 获取验证码的url
    url(r'^pc-geetest/register', views.get_geetest),
    # 专门用来校验用户名是否已被注册的接口
    url(r'^check_username_exist/$', views.check_username_exist),

    #media相关的路由设置，static内置已经写好了配置项，固定写法
    url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT}),
]
