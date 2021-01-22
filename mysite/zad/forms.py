from django import forms

from .models import  comment,post,AD
from phone_field import PhoneField, PhoneWidget

class ADForm(forms.ModelForm):
    class Meta():
        model = AD
        fields = ('Ad_title','Ad_details','photo','category',)


class PostForm(forms.ModelForm):
    class Meta():
        model = post
        fields = ('period','AD',)



class CommentForm (forms.ModelForm):
    class Meta():

        model = comment
        fields = ('comment_text',)



class ContactForm(forms.Form):
    email= forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='subject', max_length=100)
    message = forms.CharField(label='message', max_length=100)


 # phone = PhoneField(blank=False, help_text=' phone number', null=True,  wedget = forms.TextInput(attrs={'placeholder': _('phone')}))
    '''def upload_pic(request):
        if request.method=='POST':
            form=ADForm(request.POST, request.FIELS)
            if form.is_valid():
                m=AD.objects.get(pk=id)'''