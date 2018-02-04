# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import UserProfile
from .models import EmailVerifyRecord


# class UserProfileAdmin(admin.ModelAdmin):
#     """
#     注册UserProfile
#     """
#     pass

# admin.site.register(UserProfile, UserProfileAdmin)


# class EmailVerifyRecordAdmin(admin.ModelAdmin):
#     """
#     注册验证码
#     """
#     pass

# admin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
