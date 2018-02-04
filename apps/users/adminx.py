# _*_ coding: utf-8 _*_

import xadmin

from .models import EmailVerifyRecord
from .models import Banner


class EmailVerifyRecordAdmin(object):
    """
    EmailVerifyRecord注册
    """
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']
 

class BannerAdmin(object):
    """
    Banner注册
    """
    list_display = ["title", "image", "url", "index", "add_time"]
    search_fields = ["title", "url", "index"]
    list_filter = ["title", "url", "index", "add_time"]
    
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)