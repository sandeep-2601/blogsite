from django.shortcuts import render,redirect
from django.contrib import messages
from blog.models import Post
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from users.forms import *
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            uname=request.POST.get('username')
            messages.success(request,f'Registration Successful {uname}')
            return redirect('/login')
        else:
            messages.warning(request,f'Some error has occured')
            return redirect("/signin")
    else:
        form=UserRegistrationForm()
        context={'form':form}
        return render(request,'users/signin.html',context)

@login_required
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Successfully Updated')
            return redirect('profile')     
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={'u_form':u_form,'p_form':p_form}
    return render(request,'users/profile.html',context)  

def LogoutView(request):
    set_by_post=False
    if request.method =='POST':
        set_by_post=True
        logout(request)
    
    return render(request,'users/logout.html',{'set_by_post':set_by_post})