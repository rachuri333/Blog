from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .forms import (reistrationform,userupdateform,profileupdateform)

# Create your views here

def register(r):
    if r.method=="POST":
        form=reistrationform(r.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(r,f'Your Account Created Succesfully For {username}! You Can Login Now ')
            return redirect('login')
    else:
        form=reistrationform(r.POST)
    return render(r,'users/register.html',{'form':form})


@login_required
def profile(r):
    if r.method=="POST":
        u_form=userupdateform(r.POST,instance=r.user)
        p_form=profileupdateform(r.POST,r.FILES,initial=r.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(r,f'Your Account Has been Updated')
            return redirect('profile')
    else:
        u_form=userupdateform(instance=r.user)
        p_form=profileupdateform(initial=r.user.profile)
    context={
        "u_form":u_form,
        "p_form":p_form
    }
    return render(r,'users/profile.html',context)



