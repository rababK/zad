from django.shortcuts import render
from .forms import ADForm, ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import AD
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.conf import settings


def home(request):
    Ads = AD.objects.all()
    return HttpResponse(render(request, 'zad/home.html', {'Ads': Ads}))




def Add_new_AD(request):
    if request.method == 'POST':
        AD_form = ADForm(request.POST, request.FILES)
        if AD_form.is_valid():
            ad = AD_form.save(commit=False)
            ad.user = request.user
            ad.save()
            return HttpResponseRedirect(reverse('zad:home'))

        else:
            error_message = 'some data are missed'
            AD_form = ADForm()
            return render(request, 'zad/Add_AD.html', {'form': AD_form, 'error_message': error_message})
    else:
        AD_form = ADForm()
        return render(request, 'zad/Add_AD.html', {'form': AD_form})


def ContactUs(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rababkhalifamohammed@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect(reverse('zad:home'))
        return render(request, 'zad/contactUs.html', {'contact_form': contact_form})
    else:
        contact_form = ContactForm()
        return render(request, 'zad/contactUs.html', {'contact_form': contact_form})


def AD_details(request, pk):
    Ad = AD.objects.get(pk=pk)
    return render(request, 'zad/Ad_details.html', {'Ad': Ad})


def MyAd(request):
    ads = AD.objects.all()[:]
    return render(request, 'zad/My_Ad.html', {'ads': ads})




def like_Ad(request,pk):

    Ad = AD.objects.get(pk=pk)
    if Ad.likes.filter(id=request.user.id).exists():
        Ad.likes.remove(request.user)
    else:
        Ad.likes.add(request.user)
    return HttpResponseRedirect(reverse('zad:home'))



def set_language(request):
    language = request.POST.get('language', settings.LANGUAGE_CODE)
    translation.activate(language)
    request.session[translation.LANGUAGE_SESSION_KEY] = language
    return HttpResponseRedirect(reverse('zad:home'))