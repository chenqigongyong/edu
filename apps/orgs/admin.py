from django.contrib import admin
import xadmin
from .models import *

# Register your models here.
@xadmin.sites.register(CityInfo)
class CityInfoXadmin(object):
    list_display = ['name','add_time']

@xadmin.sites.register(OrgsInfo)
class OrgsInfoXadmin(object):
    list_display = ['image','name','course_num','study_num','love_num','click_num','category','cityinfo','add_time']

@xadmin.sites.register(TeacherInfo)
class TeacherInfoXadmin(object):
    list_display = ['image','name','work_year','work_position','work_style','work_company','age','gender','love_num','click_num','add_time']



