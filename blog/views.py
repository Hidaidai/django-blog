# coding: utf-8
from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from blog.models import Category
from blog.models import Tag
from datetime import datetime
from markdown import markdown
from django.http import Http404
# Create your views here.

#主页逻辑，显示博文列表
def home(request):
    post_list = Article.objects.all()  #获取全部的Article对象
    category_list = Category.objects.all() # 获取分类列表
    tag_list = Tag.objects.all() # 获取标签列表
    context = { 'post_list' : post_list , 'category_list' : category_list , 'tag_list' : tag_list }
    return render(request, 'home.html', context)

#具体博文页面逻辑，显示博文具体内容
def detail(request, id):
    category_list = Category.objects.all() # 获取分类列表
    tag_list = Tag.objects.all() # 获取标签列表
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    context = { 'post' : post , 'category_list' : category_list , 'tag_list' : tag_list }
    return render(request, 'post.html', context)

#关于“关于”页面的
def about_me(request) :
    category_list = Category.objects.all() # 获取分类列表
    tag_list = Tag.objects.all() # 获取标签列表
    context = { 'category_list' : category_list , 'tag_list' : tag_list }
    return render(request, 'aboutme.html', context)

#关于“归档”页面的
def archives(request) :
    category_list = Category.objects.all() # 获取分类列表
    tag_list = Tag.objects.all() # 获取标签列表
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    context = { 'post_list' : post_list, 'error' : False , 'category_list' : category_list , 'tag_list' : tag_list }
    return render(request, 'archives.html', context)

#关于“分类”搜索页面的
def search_category(request, category) :
    category_list = Category.objects.all() # 获取分类列表
    tag_list = Tag.objects.all() # 获取标签列表
    try:
        post_list = Article.objects.filter(category__name__exact = category) 
    except Article.DoesNotExist :
        raise Http404
    context = { 'post_list' : post_list, 'category_list' : category_list , 'tag_list' : tag_list }
    return render(request, 'category.html', context)





