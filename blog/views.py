# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def home(request):
    return HttpResponse("Hello World, Django")

def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, created_time = %s, body = %s" % (post.title, post.category, post.created_time, post.body))
    return HttpResponse(str)
