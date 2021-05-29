from django.contrib import admin
from . models import *


class AnswerInfo(admin.StackedInline):
    model = Answer
    list_display = ('id', 'user', 'forum', 'full_answer', 'date')
    extra = 2


class ForumInfo(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'full_text', 'date')
    ordering = ['date']
    inlines = [AnswerInfo]


admin.site.register(Forum, ForumInfo)

