# -*- coding: utf-8 -*-
# from django.shortcuts import render, get_object_or_404
# from .models import Post
# from .forms import PostForm
# from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from models import BBS
from django.contrib import auth


def login(request):
    return render_to_response('login.html')


def acc_login(request):
    print request.POST
    username = request.POST.get('username')
    password = request.POST.get('password')

    result = {"status": "", "data": ""}

    if username == "" or username.isspace():
        result = {"status": False, "data": "用户名不能为空"}
        return HttpResponse("username is null...")
    if password =="" or password.isspace():
        result = {"status": False, "data":"密码不能为空"}
        return HttpResponse("password is null...")

    user = auth.authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        return HttpResponse("用户名或密码不正确，请重试")


def logout(request):
    user = request.user
    auth.logout(request)
    return HttpResponse("<br>%s logout</br> <a href='/'>relogin</a>" % user)


def index(request):
    bbs_list = BBS.objects.all()
    return render_to_response('index.html', {
                              'bbs_list': bbs_list,
                              'user': request.user,  #登录成功后，前台显示用户名,(不是username?)
                              })


def bbs_detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    return render_to_response('bbs_detail.html', {
                              'bbs_obj': bbs
                              })


def sub_comment(request):
    print request.POST
    bbs_id = request.POST.get('bbs_id')
    return HttpResponseRedirect('/detail/%s/' % bbs_id)


