from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
class RegistrationForm(UserCreationForm):
    username=forms.CharField(required=True,help_text='')
    email=forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,required=True,help_text='Required')
    password2 = forms.CharField(widget=forms.PasswordInput,required=True,help_text='Required')

    class Meta:
        model=User
        fields=(
            'email',
            'username',
            'password1',
            'password2'

        )



        def save(self,commit=True):
            user=super(RegistrationForm,self).save(commit=False)
            email=self.cleaned_data['email']
            password1=self.cleaned_data['password1']
            password2=self.cleaned_data['password2']
            username=self.cleaned_data['username']
            if commit:
                user.save()
            return user
class LoginForm(forms.Form):
   username=forms.CharField(required=True,help_text="Enter Usernam")
   password=forms.CharField(required=True,widget=forms.PasswordInput)




