from django.db import models

# Create your models here.
from orgs.models import OrgsInfo, TeacherInfo


class CourseInfo(models.Model):
    iamge = models.ImageField(upload_to='course/', max_length=200, verbose_name='课程封面')
    name = models.CharField(max_length=20, verbose_name='课程名称')
    study_time = models.IntegerField(default=0,verbose_name='学习时长')
    study_num = models.IntegerField(default=0,verbose_name='学习人数')
    level = models.CharField(choices=(('gj','高级'),('zj','中级'),('cj','初级')),max_length=5,verbose_name='课程难度',default='cj')
    love_num = models.IntegerField(default=0,verbose_name='收藏数')
    click_num = models.IntegerField(default=0,verbose_name='访问量')
    desc = models.CharField(max_length=200,verbose_name='课程简介')
    detail = models.TextField(verbose_name='课程详情')
    category = models.CharField(choices=(('qd','前端开发'),('hd','后端开发')),verbose_name='课程类别',max_length=10)
    cource_notice = models.CharField(max_length=200,verbose_name='课程公告')
    cource_need = models.CharField(max_length=100,verbose_name='课程须知')
    teacher_tell = models.CharField(max_length=100,verbose_name='老师教导')
    orginfo = models.ForeignKey(OrgsInfo, verbose_name="所属机构",on_delete=models.CASCADE)
    teacherinfo = models.ForeignKey(TeacherInfo,verbose_name='所属讲师',on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now=True,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

class LessonInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name='章节名称')
    courseinfo = models.ForeignKey(CourseInfo,verbose_name='所属课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name

class VideoInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name='视频名称')
    study_time = models.IntegerField(default=0,verbose_name='视频时长')
    url = models.URLField(default='http://www.atguigu.com',verbose_name='视频链接',max_length=200)
    lessoninfo = models.ForeignKey(LessonInfo,verbose_name='所属章节',on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name

class SourceInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name='资源名称')
    down_load = models.FileField(upload_to='source/',max_length=200,verbose_name='下载路径')
    courseinfo = models.ForeignKey(CourseInfo,verbose_name='所属课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name

















