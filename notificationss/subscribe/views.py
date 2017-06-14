from django.shortcuts import render, redirect
from subscribe.forms import (
	RegistrationForm, 
	EditProfileForm
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.

def home (request):
	return render(request,'subscribe/home.html')
def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/subscribe')
	else:
		form = RegistrationForm()

		args ={'form': form}
		return render(request, 'subscribe/reg_form.html',args)
@login_required
def view_profile(request):
	args = {'user': request.user}
	return render(request, 'subscribe/profile.html', args)
@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/subscribe/profile')
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form': form}
		return render(request, 'subscribe/edit_profile.html', args)

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data =request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/subscribe/profile')
		else:
			return redirect('/subscribe/change-password')
	else:
		form = PasswordChangeForm(user = request.user)
		args = {'form': form}
		return render(request, 'subscribe/change_password.html', args)








