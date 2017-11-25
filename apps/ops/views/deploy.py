#!/usr/bin/env python
# _#_ coding:utf-8 _*_
import uuid
from django.http import HttpResponseRedirect,JsonResponse
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from ops.models import Server_Assets,Project_Config,Project_Number,Project_Order,Log_Project_Config
from utils.git import GitTools
from utils.svn import SvnTools
from utils import base
from data.DsRedisOps import DsRedis
from utils.ansible_api_v2 import ANSRunner
from django.contrib.auth.models import User,Group
from django.db.models import Count
from django.db.models import Q
from ops.tasks import recordProject,sendEmail
from django.contrib.auth.decorators import permission_required


# @login_required()
# @permission_required('OpsManage.can_add_project_config',login_url='/noperm/')
def deploy_add(request):
    if request.method == "GET":
        serverList = Server_Assets.objects.all()
        groupList = Group.objects.all()
        return render(request,'deploy/deploy_add.html',{"user":request.user,"groupList":groupList,"serverList":serverList})
    elif request.method ==  "POST":
        serverList = Server_Assets.objects.all()
        ipList = request.POST.getlist('server')
        try:
            project = Project_Config.objects.create(
                                project_name=request.POST.get('project_name'),
                                project_env=request.POST.get('project_env'),
                                project_repertory=request.POST.get('project_repertory'),
                                project_address=request.POST.get('project_address'),
                                project_repo_dir=request.POST.get('project_repo_dir'),
                                project_remote_command=request.POST.get('project_remote_command'),
                                project_local_command=request.POST.get('project_local_command'),
                                project_dir=request.POST.get('project_dir'),
                                project_uuid=uuid.uuid4(),
                                project_exclude=request.POST.get('project_exclude', '.git').rstrip(),
                                project_user=request.POST.get('project_user', 'root'),
                                project_model=request.POST.get('project_model'),
                                project_status=0,
                                project_repo_user=request.POST.get('project_repo_user'),
                                project_repo_passwd=request.POST.get('project_repo_passwd'),
                                project_audit_group=request.POST.get('project_audit_group', None),
                                )
            recordProject.delay(project_user=str(request.user),project_id=project.id,project_name=project.project_name,project_content="添加项目")
        except Exception as e:
            return render(request,'deploy/deploy_add.html',{"user":request.user,
                                                             "serverList":serverList,
                                                             "errorInfo":"部署服务器信息添加错误：%s" % str(e)})
        if ipList:
            for sid in ipList:
                try:
                    server =Server_Assets.objects.get(id=sid)
                    Project_Number.objects.create(dir=request.POST.get('dir'),server=server.ip,project=project)
                except Exception as e:
                    project.delete()
                    return render(request,'deploy/deploy_add.html',{"user":request.user,
                                                                     "serverList":serverList,
                                                                      "errorInfo":"目标服务器信息添加错误：%s" % str(e)})





def deploy_list(request):
    pass

def deploy_order(request):
    pass


def deploy_log(request):
    pass
