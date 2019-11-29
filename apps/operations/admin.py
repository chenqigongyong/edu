from django.contrib import admin
import xadmin
from operations.models import UserAsk, UserLove, UserCourse, UserComment, UserMessage

# Register your models here.
@xadmin.sites.register(UserAsk)
class UserAskXadmin(object):
    list_display = ['name','phone','course','add_time']

@xadmin.sites.register(UserLove)
class UserLoveXadmin(object):
    list_display = ['love_man','love_id','love_type','love_status','add_time']

@xadmin.sites.register(UserCourse)
class UserCourseXadmin(object):
    list_display = ['study_man','study_course','add_time']

@xadmin.sites.register(UserComment)
class UserCommentXadmin(object):
    list_display = {'comment_man', 'comment_course', 'comment_content', 'add_time'}

@xadmin.sites.register(UserMessage)
class UserMessageXadmin(object):
    list_display = ['message_man','message_content','message_status','add_time']
