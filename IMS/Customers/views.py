from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout
from .models import User
from .forms import UserRegistrationForm,CustomLoginForm,UserChangeForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def UserLogin(request):
    page_name="login"
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store:index')
    else:
        form = CustomLoginForm(request)
    return render(request, 'Customers/login_reg.html', {'form': form})

def UserRegisteration(request):
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('base:home'))
    page_name="register"
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username= form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            user.save()
            user = authenticate(username=email, password=password1)
            login(request, user)
            messages.success(request, "Registeration Successful")
        else:
            messages.error(request, "Registeration fail")
            form = UserRegistrationForm()
    return render(request, "Customers/login_reg.html", {
        'form':UserRegistrationForm(),
        'page_name': page_name
    })

def CustomLogout(request):
    logout(request)
    return redirect("store:index")



def change(request):
    if request.method == "POST":
        form = UserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse ("Done hogaya karway")
        else:
            return render(request,"Customers/login_reg.html",{
                    'page_name':"changed",
                    'form':form
                })
    return render(request,"Customers/login_reg.html",{
        'page_name':"changed",
        'form': UserChangeForm(instance=request.user)
    })