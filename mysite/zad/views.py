from django.shortcuts import render
from .forms import ADForm ,ContactForm,PostForm ,CommentForm


from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import AD,post

from django.core.mail import send_mail,BadHeaderError



def home(request):
    post.objects.all().filter(unvalid=True).delete()
    posts =post.objects.all().filter(approved=True).order_by('vote')[:]


    if request.user.is_authenticated and request.user.is_staff:
        return HttpResponse(render(request, 'admin_home.html', {'posts': posts}))
    else:
        return HttpResponse(render(request, 'zad/home.html', {'posts': posts}))




def Add_new_AD(request):
    if request.method == 'POST':
        AD_form = ADForm(request.POST,request.FILES)
        if AD_form.is_valid():
            ad=AD_form.save(commit=False)
            print(ad.id)
            print(ad.photo)
            return HttpResponseRedirect(reverse('zad:home'))

        else:
            error_message = 'some data are missed'
            AD_form = ADForm()
            return render(request, 'zad/Add_AD.html', {'form': AD_form,'error_message':error_message})
    else:
        AD_form = ADForm()
        return render(request, 'zad/Add_AD.html', {'form': AD_form})





def ContactUs(request):
    if request.method=='POST':
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


def post_details (request, pk):
    POST = post.objects.get(pk = pk)
    return render(request, 'zad/post_details.html', {'post': POST})


def MyAd (request):
    ads = AD.objects.all()[:]
    return render(request, 'zad/My_Ad.html', {'ads': ads})



def Add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST,request.FILES)
        if post_form.is_valid():
            post= post_form.save(commit=False)
            post.user = request.user
            post.save()


            return HttpResponseRedirect(reverse('zad:home'))
        else:
            error_message = 'some data are missed'
            post_form = PostForm()
            return render(request, 'zad/Add_post.html', {'form': post_form,'error_message':error_message})
    else:
        post_form = PostForm()
        return render(request, 'zad/Add_post.html', {'form': post_form})

def Add_comment(request,pk):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment= comment_form.save(commit=False)
            comment.post = post.objects.get(pk=pk)
            comment.save()


            return HttpResponseRedirect(reverse('zad:home'))
        else:
            error_message = 'some data are missed'
            comment_form = CommentForm()
            return render(request, 'zad/add_comment.html', {'form': comment_form,'error_message':error_message})
    else:
        comment_form = CommentForm()
        return render(request, 'zad/add_comment.html', {'form': comment_form})
