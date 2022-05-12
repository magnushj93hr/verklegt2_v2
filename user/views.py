from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileForm
from user.models import Profile


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })


def profile(request):
    profile = Profile.objects.filter(user=request.user).first() #hvaða fyrstu færslu?
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile= form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
            ##MÖGULEGA BERYTA I 'NAME' OG EKKI 'USER'??
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


def change_name(request):
    new_name = request.POST.get('new_name')

    if User.objects.filter(username=new_name).exists():
        raise forms.ValidationError('Username "%s" is not available.' % new_name)
    user = request.user
    user.username = new_name
    user.save()
    return redirect('profile')
