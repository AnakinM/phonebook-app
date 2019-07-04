from django import forms
from .models import Person, Phone, Email

class ContactForm(forms.Form):
    first_name  = forms.CharField()
    last_name   = forms.CharField()
    phone       = forms.CharField()
    email       = forms.EmailField()

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name']

class PhoneModelForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone']

class EmailModelForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']