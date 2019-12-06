#from django.contrib import admin

# Register your models here.
import xadmin
from .models import BannerInfo, EmailVerifyCode
from xadmin import views

#配置xadmin主题
@xadmin.sites.register(views.BaseAdminView)
class BaseXadminSetting(object):
    enable_themes = True
    use_bootswatch = True

#页眉、页脚、菜单设置
@xadmin.sites.register(views.CommAdminView)
class CommonXamdinSetting(object):
    site_title = 'xx教育后台管理平台'
    site_footer = 'xxIT教育'
    menu_style = 'accordion'

#轮播图表
@xadmin.sites.register(BannerInfo)
class BannerInfoXadmin(object):
    list_display = ['image','url','add_time']

#验证码
@xadmin.sites.register(EmailVerifyCode)
class EmailVerifyCodeXadmin(object):
    list_display = ['code','email','send_type','add_time']

