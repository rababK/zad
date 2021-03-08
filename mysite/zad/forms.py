from django import forms

from .models import  AD


class ADForm(forms.ModelForm):
    class Meta():
        model = AD
        fields = ('Ad_title','Ad_details','category','photo','term')



class ContactForm(forms.Form):
    email= forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', max_length=100)


