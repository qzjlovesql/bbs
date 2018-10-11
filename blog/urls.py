from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'(\w+)/article/(\d+)/$',views.article_detail), #文章详情
    url(r'(?P<username>\w+)',views.home), #home(request,username)分组命名匹配
]