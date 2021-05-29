from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class BlockInfo(models.Model):
    title = models.CharField('Название', max_length=50)
    anons_img = RichTextUploadingField('Картинка анонса', null=True, blank=True)
    anons = RichTextUploadingField('Анонс', max_length=240)
    image = models.ImageField(upload_to='main', verbose_name='Изображение', null=True, blank=True, )
    history = RichTextUploadingField('История происхождения породы собаки', null=True, blank=True)
    characteristic = RichTextUploadingField('Характеристики породы', null=True, blank=True)
    height = models.CharField('Рост', max_length=30, null=True, blank=True)
    weight = models.CharField('Вес', max_length=30, null=True, blank=True)
    age = models.CharField('Продолжительность жизни', max_length=30, null=True, blank=True)
    pet_care = RichTextUploadingField('Уход за питомцем', null=True, blank=True)
    nails = RichTextUploadingField('Стрижка когтей', null=True, blank=True)
    teeth = RichTextUploadingField('Чистка зубов', null=True, blank=True)
    wool = RichTextUploadingField('Вычесывание шерсти', null=True, blank=True)
    bathe = RichTextUploadingField('Купание', null=True, blank=True)
    eyes_ears = RichTextUploadingField('Чистка глаз и ушей',  null=True, blank=True)
    general_info = RichTextUploadingField('Общая информация', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информационный блок про породу собаки'
        verbose_name_plural = 'Информационные блоки про породы собак'


#class ImageGallery(models.Model):
    #image = models.ImageField(upload_to='main', verbose_name='Изображение', null=True, blank=True,)
    #image_id = models.PositiveSmallIntegerField(default=1, blank=True, null=True,)
   # block_info = models.ForeignKey(BlockInfo, verbose_name='Порода собаки', on_delete=models.CASCADE,
                                   #related_name='images')

    #class Meta:
        #verbose_name = 'файл'
        #verbose_name_plural = 'Галерея картинок'



