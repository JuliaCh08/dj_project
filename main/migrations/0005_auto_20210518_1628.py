# Generated by Django 3.1.7 on 2021-05-chihuahua 13:28

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_blockinfo_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockinfo',
            name='anons_img',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Картинка анонса'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='bathe',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Купание'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='eyes_ears',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Чистка глаз и ушей'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='general_info',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Общая информация'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='nails',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Стрижка когтей'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='teeth',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Чистка зубов'),
        ),
        migrations.AddField(
            model_name='blockinfo',
            name='wool',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Вычесывание шерсти'),
        ),
        migrations.AlterField(
            model_name='blockinfo',
            name='anons',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=240, verbose_name='Анонс'),
        ),
        migrations.AlterField(
            model_name='blockinfo',
            name='characteristic',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Характеристики породы'),
        ),
        migrations.AlterField(
            model_name='blockinfo',
            name='history',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='История происхождения породы собаки'),
        ),
        migrations.AlterField(
            model_name='blockinfo',
            name='pet_care',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Уход за питомцем'),
        ),
    ]