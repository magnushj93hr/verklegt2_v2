from django.contrib.auth.forms import UserCreationForm
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
    current_user = request.user
    print(current_user.username)
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

