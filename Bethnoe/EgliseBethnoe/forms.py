# -*- coding: utf8 -*- 
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.core.validators import validate_email


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
		


class ContactForm(forms.Form):
    nameField = forms.CharField(label='Votre nom', max_length=100)
    firstNameField = forms.CharField(label='Votre prénom', max_length=100)
    emailField = forms.EmailField(label='Votre email', required=True, validators=[validate_email])
    descField = forms.CharField(label='Votre message', widget=forms.Textarea())
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))
    def clean(self):
    	cleaned_data = super(ContactForm, self).clean()
    	nameField = cleaned_data.get("nameField")
    	firstNameField = cleaned_data.get("firstNameField")
    	emailField = cleaned_data.get("emailField")
    	descField = cleaned_data.get("descField")
        if len(nameField) < 5:
            msg_nameField = u"le nom doit contenir plus de 2 caracteres"
            self.add_error('nameField', msg_nameField)
        if len(firstNameField) < 5:
            msg_firstNameField = u"le prenom doit contenir plus de 2 caracteres"
            self.add_error('firstNameField', msg_firstNameField)
        if not '@' in emailField:    
            msg_emailField = u"le mail doit contenir @"
            self.add_error('emailField', msg_emailField)
        return cleaned_data
	class Meta:
		widgets = {		
		'nameField': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
		'firstNameField': forms.TextInput(attrs={'class': 'form-control col-md-6'}), 
		'login': forms.TextInput(attrs={'class': 'form-control col-md-6'}), 
		'emailField': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
		}
		