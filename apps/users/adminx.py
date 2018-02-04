# _*_ coding: utf-8 _*_

import xadmin
from xadmin import views

from .models import EmailVerifyRecord
from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"慕学后台管理系统"
    site_footer = u"慕学在线网"
    menu_style = "accordion"


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
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)