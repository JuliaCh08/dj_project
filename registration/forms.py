from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    username = forms.CharField(min_length=2, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    email = forms.EmailField(min_length=7, max_length=50, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("Вы должны подтвердить свой пароль")
        if password1 != password2:
            raise forms.ValidationError("Ваши пароли не совпадают")
        return password2


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserProfileForm(forms.ModelForm):

    avatar = forms.ImageField(widget=forms.ClearableFileInput(),
                              required=False, label=u'Аватар')

    class Meta:
        model = UserProfile
        fields = ('avatar', 'user',)


