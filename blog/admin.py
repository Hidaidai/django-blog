# coding: utf-8
from django.contrib import admin
from blog.models import Article
from blog.models import Category
#从blog的models类中引入Article类
import sys;
reload(sys);
sys.setdefaultencoding("utf8")
#讲后台输入的信息转为utf-8形式

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
