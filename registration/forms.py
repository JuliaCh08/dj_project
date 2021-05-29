from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(min_length=7, max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean(self):
        # Определяем правило валидации
        if self.cleaned_data.get('password1') != self.cleaned_data.get('password2'):
            # Выбрасываем ошибку, если пароли не совпали
            raise forms.ValidationError('Пароли не совпадают!')
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserProfileForm(forms.ModelForm):

    avatar = forms.ImageField(widget=forms.ClearableFileInput(),
                              required=False, label=u'Аватар')

    class Meta:
        model = UserProfile
        fields = ('avatar', 'user',)


