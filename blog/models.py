# coding: utf-8
from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = '分类'

class Tag(models.Model):
    tag_name = models.CharField('标签', max_length=20)
    def __unicode__(self):
        return self.tag_name
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '已发布'),
    )
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=False)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.TextField('摘要', max_length=200, blank=True, null=True, help_text="可选，如若为空将摘取正文的前200个字符")
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField('Tag', verbose_name='标签', blank=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-last_modified_time']
        verbose_name = '博文'
        verbose_name_plural = '博文'
