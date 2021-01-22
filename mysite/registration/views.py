import os
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserProfile, Account
from .forms import  AccountCreationForm
from .forms import UserProfileForm
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def home (request):
	return render(request, 'registration/home.html')

def register(request):
	if request.method == 'POST':
		user_form = AccountCreationForm(request.POST, request.FILES)
		profile_form = UserProfileForm(request.POST, request.FILES)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save(commit=False)
			raw_password = user.password
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			# logging in user after completing registration
			user = auth.authenticate(username=user.email, password=raw_password)
			auth.login(request, user)
			return HttpResponseRedirect(reverse('registration:home'))
		else:
			print(user_form.errors)
			print(profile_form.errors)

	else:
		user_form = AccountCreationForm()
		profile_form = UserProfileForm()

	context = {
		'user_form' : user_form,
		'profile_form': profile_form,
	}

	return render(request, 'registration/register.html', context=context)



def login(request):
	if request.method == 'POST':
		username = request.POST.get('email')
		password = request.POST.get('password')

		user = auth.authenticate(username=username, password=password)

		if user:
			if user.is_active:
				auth.login(request, user)
				return HttpResponseRedirect(reverse('home'))
			return HttpResponse('Your id is inactive i.e. disabled')
		return HttpResponse('Invalid login details provided')

	# i.e. method is get
	context = {}
	return render(request, 'registration/login.html', context=context)



def logout(request):
	auth.logout(request)
	return HttpResponseRedirect(reverse('home'))



def process_profile_picture_name(name):
	new_name = os.path.split(name)[1]
	return new_name.split('_', 1)[1]

def profile(request, email):
	try:
		user = User.objects.get(email=email)
	except User.DoesNotExist:
		raise Http404("user not found")

	profile = UserProfile.objects.get(user=user)
	if profile.picture:
		profile.picture.new_name = process_profile_picture_name(profile.picture.name)
	context = {
		'profile' : profile
	}

	return render(request, 'registration/profile.html', context=context)
