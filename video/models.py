from django.db import models
from embed_video.fields import EmbedVideoField


class Videos(models.Model):
    title = models.CharField('Название видео', max_length=100)
    video = EmbedVideoField('Видео', blank=True)
    date = models.DateTimeField('Дата добавления видео')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'

# Create your models here.
