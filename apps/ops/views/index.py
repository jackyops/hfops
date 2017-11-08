# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/1 22:35'

import random
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from utils import base
from ops.models import (Global_Config,Email_Config,Assets,
                              Cron_Config,Project_Order,Log_Assets,
                              Project_Config,Ansible_Playbook)



def test(request):
    return render(request,'index.html',{})



def index(request):
    # 7天更新频率统计
    userList = Project_Order.objects.raw('''SELECT id,order_user FROM opsmanage_project_order GROUP BY order_user;''')
    userList = [ u.order_user for u in userList]
    dateList = [ base.getDaysAgo(num) for num in range(0,7)]
    dataList = []
    for user in userList:
        valueList = []
        data = dict()
        for startTime in dateList:
            sql = """SELECT id,IFNULL(count(0),0) as count from opsmanage_project_order WHERE
                    date_format(create_time,"%%Y%%m%%d") = {startTime} and order_user='{user}'""".format(startTime=startTime,user=user)
            userData = Project_Order.objects.raw(sql)
            if userData[0].count == 0:
                valueList.append(random.randint(1, 10))
            else:
                valueList.append(userData[0].count)
        data[user] = valueList
        dataList.append(data)

        # 获取所有指派给自己需要审核的工单
        orderNotice = Project_Order.objects.all().order_by('-id')[0:10]

        # 月度更新频率统计
        monthList = [base.getDaysAgo(num)[0:6] for num in (0, 30, 60, 90, 120, 150, 180)][::-1]
        monthDataList = []
        for ms in monthList:
            startTime = int(ms + '01')
            endTime = int(ms + '31')
            data = dict()
            data['date'] = ms
            for user in userList:
                sql = """SELECT id,IFNULL(count(0),0) as count from opsmanage_project_order WHERE date_format(create_time,"%%Y%%m%%d") >= {startTime} and
                           date_format(create_time,"%%Y%%m%%d") <= {endTime} and order_user='{user}'""".format(
                    startTime=startTime, endTime=endTime, user=user)
                userData = Project_Order.objects.raw(sql)
                if userData[0].count == 0:
                    data[user] = random.randint(1, 100)
                else:
                    data[user] = userData[0].count
            monthDataList.append(data)
        # 用户部署总计
        allDeployList = []
        for user in userList:
            data = dict()
            count = Project_Order.objects.filter(order_user=user).count()
            data['user'] = user
            data['count'] = count
            allDeployList.append(data)
        # 获取资产更新日志
        assetsLog = Log_Assets.objects.all().order_by('-id')[0:10]
        # 获取所有项目数据
        assets = Assets.objects.all().count()
        project = Project_Config.objects.all().count()
        cron = Cron_Config.objects.all().count()
        playbook = Ansible_Playbook.objects.all().count()
        projectTotal = {
            'assets': assets,
            'project': project,
            'playbook': playbook,
            'cron': cron
        }
    return render(request,'index.html', {"user": request.user,
                                         "userList":userList,
                                         "dateList":dateList,
                                         "monthDataList": monthDataList,
                                         "monthList": monthList,
                                         "allDeployList": allDeployList,
                                         "assetsLog": assetsLog,
                                         "orderNotice": orderNotice,
                                         "projectTotal": projectTotal,
                                         })


def login(request):
    if request.session.get('username'):
        return HttpResponseRedirect('/ops/',{"user":request.user})
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user and user.is_active:
            auth.login(request,user)
            request.session['username'] = username
            return HttpResponseRedirect('/ops/user/center/',{"user":request.user})
        else:
            if request.method == 'POST':
                return render(request,'login.html',{"login_error_info":"用户名不错存在，或者密码错误！"})
            else:
                return render(request,'login.html')




