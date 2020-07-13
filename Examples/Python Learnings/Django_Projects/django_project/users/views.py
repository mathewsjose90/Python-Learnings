from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    print(request.method)
    if request.method.upper() == 'POST':
        form = UserRegisterForm(request.POST)
        print('Going to validate form')

        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your Account is created {0}. Please can now login !'.format(username))
            print('Going to re-direct')
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
        messages.success(request, 'Your account has been updated !!!')
        return redirect('users:users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form}

    return render(request, 'users/profile.html', context)
