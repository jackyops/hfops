# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/1 21:29'

import xadmin
from xadmin import views


class BaseSetting(object):
    #启用主题
    enable_themes = True
    #添加多种主体
    use_bootswatch = True

class GlobalSetting(object):
    site_title = "华付运维"
    site_footer = "华付信息技术有限公司"
    #缩放菜单
    menu_style = "accordion"





xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)