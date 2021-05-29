from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile


class UserInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Доп. информация'


# Определяем новый класс настроек для модели User
class UserAdmin(UserAdmin):
    inlines = (UserInline,)


# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


"""class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_avatar']

    def get_avatar(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} width="80" height="80">')

    get_avatar.short_description = "Аватар пользователя"


admin.site.register(UserProfile, UserProfileAdmin)"""
# Register your models here.
