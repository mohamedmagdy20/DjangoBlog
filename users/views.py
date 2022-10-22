from email import message
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileRegister, ProfileUpdateForm, UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
        if request.method == 'POST':
            user_form = UserRegisterForm(request.POST)
            profile_form = ProfileRegister(request.POST,request.FILES)
            if user_form.is_valid() and  profile_form.is_valid():
                user = user_form.save()
                profile =  profile_form.save(commit=False)
                profile.user = user
                profile.save()
                username = user_form.cleaned_data.get('username')
                messages.success(request,f'Account Created for {username} ') 
                return redirect('blog_home')          
        else:
            user_form = UserRegisterForm()       
            profile_form = ProfileRegister()
        return render(request,'users/register.html',{'user_form':user_form,'profile_form':profile_form})

    
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request,'Account Updated') 
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    return render(request,'users/profile.html',{"u_form":u_form,"p_form":p_form})


# def userUpdate(request):
#     if(request.method == POST):
