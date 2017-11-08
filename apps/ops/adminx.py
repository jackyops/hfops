# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/1 23:24'




import xadmin
from .models import *
xadmin.site.register(Assets)
xadmin.site.register(Server_Assets)
xadmin.site.register(Network_Assets)
xadmin.site.register(Disk_Assets)
xadmin.site.register(Ram_Assets)
xadmin.site.register(NetworkCard_Assets)
xadmin.site.register(Service_Assets)
xadmin.site.register(Zone_Assets)
xadmin.site.register(Line_Assets)
xadmin.site.register(Raid_Assets)
xadmin.site.register(Log_Assets)
xadmin.site.register(Project_Config)
xadmin.site.register(Log_Project_Config)
xadmin.site.register(Project_Number)
xadmin.site.register(Project_Order)
xadmin.site.register(Cron_Config)
xadmin.site.register(Log_Cron_Config)
xadmin.site.register(Log_Ansible_Model)
xadmin.site.register(Log_Ansible_Playbook)
xadmin.site.register(Ansible_Playbook_Number)
xadmin.site.register(Global_Config)
xadmin.site.register(Email_Config)
xadmin.site.register(Server_Command_Record)
xadmin.site.register(Ansible_CallBack_Model_Result)
xadmin.site.register(Ansible_CallBack_PlayBook_Result)