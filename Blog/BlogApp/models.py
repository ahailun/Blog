# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class BBS(models.Model):                                   #帖子
    title = models.CharField(max_length=64)                #帖子标题
    summery = models.CharField(max_length=256, blank=True) #帖子概要信息，可以为空
    content = models.TextField()                           #帖子内容
    author = models.ForeignKey('BBS_user')                 #帖子作者
    view_count = models.IntegerField()                     #帖子的浏览数
    ranking = models.IntegerField()                        #置顶排名
    creat_at = models.DateTimeField()                      #本帖子创建日期
    updated_at = models.DateTimeField()                    #本帖子修改日期

    def __unicode__(self):
        return self.title


class Category(models.Model):                              #板块名称,如分为：体育、车展、政要等几类
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user')


class BBS_user(models.Model):
    user = models.OneToOneField(User)
    signature = models.CharField(max_length=128, default="this guy is too lazy to leave anything here.")  #每个用户的签名，如QQ的说说
    photo = models.ImageField(upload_to=".\BlogApp\static\img", default='.\BlogApp\static\img\BMW.jpg')

    def __unicode__(self):
        return self.user.username
