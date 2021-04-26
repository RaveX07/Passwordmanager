from django import forms

from .models import Password, User

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = [
            'Benutzer',
            'Passwort',
            'WebsiteURL',
            'WebsiteName'
        ]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'Name',
            'Email',
            'Passwort'       
        ]
