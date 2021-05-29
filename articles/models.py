from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = RichTextUploadingField('Анонс', max_length=270)
    image = models.ImageField(upload_to='articles', verbose_name='Изображение', null=True, blank=True, )
    full_text = RichTextUploadingField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'



