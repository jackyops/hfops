# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/1 22:30'

from django.conf.urls import  url, include
from ops.views import index,users,assets
from restfull.assets_api import *

urlpatterns = [
    url(r'^$', index.index,name="index"),
    url(r'^login/',index.login),
    url(r'^user/center/$',users.user_center),
    url(r'^assets_config/$',assets.assets_config,name="assets_config"),
    url(r'^assets_add/$',assets.assets_add,name="assets_add"),
    url(r'^assets_list/$',assets.assets_list,name="assets_list"),
    url(r'^assets_search/$',assets.assets_search,name="assets_search"),
    url(r'^assets_log/$',assets.assets_log,name="assets_log"),
    url(r'^assets_view/(?P<aid>[0-9]+)/$',assets.assets_view,name="assets_view"),
    url(r'^assets_facts',assets.assets_facts,name="assets_facts"),

    url(r'^api/service/$',service_list,name="service_list"),
    url(r'^api/service/(?P<id>[0-9]+)/$', service_detail,name="service_detail"),
    url(r'^api/group/$', group_list,name="group_list"),
    url(r'^api/group/(?P<id>[0-9]+)/$', group_detail,name="group_detail"),
    url(r'^api/zone/$', zone_list,name="zone_list"),
    url(r'^api/zone/(?P<id>[0-9]+)/$', zone_detail,name="zone_detail"),
    url(r'^api/line/$', line_list,name="line_list"),
    url(r'^api/line/(?P<id>[0-9]+)/$',line_detail,name="line_detail"),
    url(r'^api/raid/$', raid_list,name="raid_list"),
    url(r'^api/raid/(?P<id>[0-9]+)/$',raid_detail,name="raid_detail"),
    url(r'^api/server/$', asset_server_list,name="asset_server_list"),
    url(r'^api/server/(?P<id>[0-9]+)/$', asset_server_detail,name="asset_server_detail"),
    url(r'^api/net/$', asset_net_list,name="asset_net_list"),
    url(r'^api/net/(?P<id>[0-9]+)/$', asset_net_detail,name="asset_net_detail"),


    url(r'^api/server/$', asset_server_list,name="asset_server_list"),
    url(r'^api/server/(?P<id>[0-9]+)/$', asset_server_detail,name="asset_server_detail")
]