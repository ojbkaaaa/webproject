# 用户注册表单
from django import forms
from django.db import models

from .models import User_info

class User_infoForm(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ('name', 'pwd', 'email', 'phone', 'common')


class LoginFrom(forms.Form):
    username = forms.CharField(max_length=10, label='用户')
    password = forms.CharField(max_length=20, label='密码')
