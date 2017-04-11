# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.models import Category
from blog.models import Tag
from datetime import datetime
from markdown import markdown
from django.http import Http404

# Create your views here.

#模板页面，显示标签和分类
def model(request):
    tag_list = Tag.objects.all()
    return render(request, 'base.html', {'tag_list' : tag_list})

#主页逻辑，显示博文列表
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

#具体博文页面逻辑，显示博文具体内容
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})

#关于“关于”页面的
def about_me(request) :
    return render(request, 'aboutme.html')

#关于“归档”页面的
def archives(request) :
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'archives.html', {'post_list' : post_list, 'error' : False})

#关于“标签”搜索页面的
def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})





