# _*_ coding: utf-8 _*_

import xadmin

from .models import Course
from .models import Lesson
from .models import Video
from .models import CourseResource


class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "learn_times", "students", "fav_nums", "click_nums", "add_time"]
    search_fields = ["name", "desc", "detail", "learn_times", "students", "fav_nums", "click_nums"]
    list_filter = ["name", "desc", "detail", "learn_times", "students", "fav_nums", "click_nums"]


class LessonAdmin(object):
    list_display= ["course", "name", "add_time"]
    search_fields = ["course", "name"]
    list_filter = ["course", "name"]


class VideoAdmin(object):
    list_display = ["lesson", "name", "add_time"]
    search_fields = ["lesson", "name"]
    list_filter = ["lesson", "name"]


class CourseResourceAdmin(object):
    list_display = ["course", "name", "download"]
    search_fields = ["course", "name", "download"]
    list_filter = ["course", "name", "download"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
