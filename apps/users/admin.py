#from django.contrib import admin

# Register your models here.
import xadmin
from .models import BannerInfo, EmailVerifyCode

#轮播图表
@xadmin.sites.register(BannerInfo)
class BannerInfoXadmin(object):
    list_display = ['image','url','add_time']

#验证码
@xadmin.sites.register(EmailVerifyCode)
class EmailVerifyCodeXadmin(object):
    list_display = ['code','email','send_type','add_time']

