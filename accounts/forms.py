from django import forms 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 
from captcha.fields import ReCaptchaField
from bankaccounts.models import KYC
from django.forms import FileInput

class user_form(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"Email"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password"}))
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
    captcha = ReCaptchaField()

class KYC_form(forms.ModelForm):
    identity_image=forms.ImageField(widget=FileInput)
    image=forms.ImageField(widget=FileInput)
    signature=forms.ImageField(widget=FileInput)
    class Meta:
      model=KYC
      fields=[
         'full_name',
         'image',
         'marital_status',
         'gender',
         'identity_type',
         'identity_image',
         'date_of_birth',
         'signature',
         'country',
         'state',
         'city',
         'phone',
         'email'

      ]