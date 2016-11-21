# -*- coding: utf8 -*- 
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms

class UserForm(forms.ModelForm): 
	class Meta:
		model = User
		fields = ['last_name', 'first_name', 'email', 'username', 'password']
		exclude = ['groups', 'is_staff', 'is_active', 'user_permissions', 'last_login', 'date_joined', 'is_superuser']
		
		widgets = {'password': forms.PasswordInput(attrs={'class': 'form-control col-md-6'}), 'username': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
		'last_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}), 'first_name': forms.TextInput(attrs={'class': 'form-control col-md-6'}), 
		'login': forms.TextInput(attrs={'class': 'form-control col-md-6'}), 'email': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
		}
		help_texts = {'login': _('Sans caracteres speciaux '),'username': _('Sans caracteres speciaux '), 'last_name': _('Sans caracteres speciaux '), 'first_name': _('Sans caracteres speciaux '),
		'email': _('Sans caracteres speciaux '), 'password': _('Sans caracteres speciaux '),
		}
		


