# -*- coding: utf-8 -*-
__author__ = 'Jacky'
__date__ = '2017/11/1 22:42'

import time
from datetime import datetime,timedelta

def getDaysAgo(num):
    threeDayAgo = (datetime.now() - timedelta(days = num))
    timeStamp = int(time.mktime(threeDayAgo .timetuple()))
    otherStyleTime = threeDayAgo .strftime("%Y%m%d")
    return otherStyleTime
