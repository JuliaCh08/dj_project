from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    avatar = models.ImageField('Аватар пользователя', default='../profile_avatar/emptyAvatar.jpg',
                               upload_to='profile_avatar', blank=True, null=True)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


