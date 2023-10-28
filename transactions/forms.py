from transactions.models import Credit_Card
from django import forms

class Creditcard_Form(forms.ModelForm):
    class Meta:
        model=Credit_Card
        fields=['user','name','number','month','year','cvv','card_type','card_status']