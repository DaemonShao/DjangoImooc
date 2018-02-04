# _*_ coding: utf-8 _*_

import xadmin

from .models import EmailVerifyRecord


class EmailVerifyRecordAdmin(object):
    """
    EmailVerifyRecord注册
    """
    pass

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
