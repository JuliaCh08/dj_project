from django.contrib import admin
from . models import Articles


class ArticlesInfo(admin.ModelAdmin):
    list_display = ('title',  'date')
    list_filter = ('date',)
    search_fields = ('title',)


# admin.site.register(Articles)


admin.site.register(Articles, ArticlesInfo)
