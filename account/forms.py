from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUserModel



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUserModel
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUserModel
        fields = ('email',)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "id":"exampleInputEmail1", "placeholder":"Enter email/username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "id":"exampleInputPassword1", "placeholder":"Password"}))

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name','last_name', 'email', 'birth_date', 'gender', 'avatar')

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Passwords don\'t match ')
        return data['password']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('username', 'first_name','last_name', 'email', 'birth_date', 'gender', 'avatar')
