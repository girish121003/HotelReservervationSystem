from django.shortcuts import render,render_to_response,redirect
from django.http import HttpResponseRedirect, HttpResponse
from Reserve.models import Room,Roomtype
from django.template import context, loader
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.forms import UserCreationForm,forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Reserve.forms import RegistrationForm,LoginForm


def index(request):
     return render(request,'Reserve/index.html')
def signup(request):
        form=RegistrationForm()
        if request.method=='POST':
          form=RegistrationForm(request.POST)
          if form.is_valid():
              form.save(commit=True)
              return index(request)
        return render(request, 'Reserve/SignUpForm.html',{'form':form})

@login_required
def user_logout(request):
    logout(request)
    return  HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'),{'user':username})

            else:
                print("not active")
                return HttpResponse("Account Not Active!")

        else:
            print("invalid credential")
            return HttpResponse("Invalid Credentials!!")
    else:

        return render(request,'Reserve/login.html',{})
def search_room(request):
        room=Roomtype.objects.all()
        return render(request,'Reserve/SearchHotel.html',{'rooms':room})

