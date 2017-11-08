# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/2 10:36'

from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from users.models import UserProfile

from ops.models import Project_Order




def user_center(request):
    if request.method == "GET":
        orderList = Project_Order.objects.filter(Q(order_user=UserProfile.objects.get(username=request.user)) |
                                                Q(order_audit=UserProfile.objects.get(username=request.user))).order_by("id")[0:150]
        return render(request,'users/user_center.html',{"user":request.user,"orderList":orderList})
    if request.method == "POST":
        if request.POST.get('password') == request.POST.get('c_password'):
            try:
                user = User.objects.get(username=request.user)
                user.set_password(request.POST.get('password'))
                user.save()
                return JsonResponse({"code":200,"data":None,"msg":"密码修改成功"})
            except Exception as e:
                return JsonResponse({"code":500,"data":None,"msg":"密码修改失败：%s" % str(e)})
        else:return JsonResponse({"code":500,"data":None,"msg":"密码不一致，密码修改失败。"})