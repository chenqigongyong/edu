from django.contrib import admin
import xadmin
# Register your models here.
from courses.models import CourseInfo, LessonInfo, VideoInfo, SourceInfo


@xadmin.sites.register(CourseInfo)
class CourseInfoXadmin(object):
    list_display = ['iamge','name','study_time','study_num','level','love_num','click_num','orginfo','teacherinfo','add_time']

@xadmin.sites.register(LessonInfo)
class LessonInfoXadmin(object):
    list_display = ['name','courseinfo','add_time']

@xadmin.sites.register(VideoInfo)
class VideoInfoXadmin(object):
    list_display = ['name','study_time','url','lessoninfo','add_time']

@xadmin.sites.register(SourceInfo)
class SourceInfoXadmin(object):
    list_display = ['name','down_load','courseinfo','add_time']

