
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField, CaptchaTextInput


from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Games
        fields = ['title', 'slug', 'content', 'photo', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 12, 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': "form-control"}),
            'cat': forms.Select(attrs={'class': 'form-select'})
        }

    #Validator na title
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        else:
            return title


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', max_length=40, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='Пройдите проверку')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control mx-sm-3'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control mx-sm-3'}))
    captcha = CaptchaField(label='Пройдите проверку')


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control mx-sm-3'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control mx-sm-3'}))
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols': 50, 'rows': 8, 'class': 'form-control mx-sm-3'}))
    captcha = CaptchaField(label='Пройдите проверку')


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Контент',widget=forms.Textarea(attrs={'cols': 50, 'rows': 3, 'class': 'form-control mx-sm-3'}))
    class Meta:
        model = Comment
        fields = ('body',)

