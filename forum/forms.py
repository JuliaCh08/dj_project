from .models import Forum, Answer
from django.forms import ModelForm, TextInput, Textarea


class ForumForm(ModelForm):

    class Meta:
        model = Forum
        fields = ['id', 'author', 'title', 'full_text', 'date']
        widgets = {
            "title": TextInput(attrs={
                'class': 'type-field',
                'placeholder': 'Тема вопроса'}),
            "full_text": Textarea(attrs={
                'class': 'type-field',
                'placeholder': 'Напишите свой вопрос'}),
        }


class AnswerForm(ModelForm):

    class Meta:
        model = Answer
        fields = ['id', 'user', 'forum', 'full_answer', 'date']
        widgets = {
            "full_answer": Textarea(attrs={
                'class': 'type-field',
                'placeholder': 'Напишите свой ответ'}),
        }


