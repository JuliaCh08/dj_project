from django.db import models
import datetime



class Forum(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('Тема вопроса', max_length=150)
    full_text = models.TextField('Блок с вопросом')
    date = models.DateTimeField('Дата создания вопроса', default=datetime.datetime.now, blank=True)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Информационный блок  из форума'
        verbose_name_plural = 'Информационные блоки из форума'


class Answer(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, blank=True, null=True)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='answers', blank=True, null=True)
    full_answer = models.TextField('Блок с ответом')
    date = models.DateTimeField('Дата создания ответа', default=datetime.datetime.now, blank=True)

    def __str__(self):
        return f'Ответ {self.user} на вопрос: {self.forum}'

    class Meta:
        verbose_name = 'Ответ на вопрос из форума'
        verbose_name_plural = 'Ответы на вопросы из форума'




