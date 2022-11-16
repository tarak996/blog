from django.shortcuts import render,HttpResponseRedirect
from .forms import singup,formBlog
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from . models import modelBlog
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
# Create your views here.

def homeblog(request):
    home=modelBlog.objects.all()
    return render(request,'home.html',{'blog':home})

def contact(request):

    return render(request,'contact.html')

def sing(request):
    if request.method=='POST':
        obj=singup(request.POST)
        if obj.is_valid():
            Email=obj.cleaned_data['email']
            obj.save()
            messages.success(request,'successfully singup')
            send_mail(
                'Testing mail',
                'hi this is my first mail using python',
                'tarakn996@gmail.com',
                [str(Email)],
                fail_silently=False)

            obj=singup()
    else:
        obj=singup()
    return render(request,'singup.html',{'form':obj})




def login1(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            obj=AuthenticationForm(request=request,data=request.POST)
            if obj.is_valid():
                uname=obj.cleaned_data['username']
                upass=obj.cleaned_data['password']
                user=authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'successfully login')
                    return HttpResponseRedirect('/profile')
        else:
            obj=AuthenticationForm()
        return render(request,'login.html',{'form':obj})
    else:
        return HttpResponseRedirect('/profile')

def profile(request):
    fm=formBlog
    if request.method=='POST':
        obj = formBlog(request.POST)
        if obj.is_valid():
            obj.save()
            messages.success(request, 'successfully singup')
            obj = formBlog()
            home = modelBlog.objects.all()

            return HttpResponseRedirect('/')
    else:
        fm=formBlog()
    return render(request, 'singup.html', {'form': fm})

    #return  HttpResponseRedirect('/')


def edit1(request,id):
    fm=modelBlog.objects.get(pk=id)
    form=formBlog(instance=fm)
    if request.method=='POST':
        form=formBlog(request.POST,instance=fm)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/home')
    else:
        return render(request,'edit.html',{'form':form})

def delete1(request,id):
    fm=modelBlog.objects.get(pk=id)
    fm.delete()
    return HttpResponseRedirect('/home')

def about(request):
    return render(request,'aboutus.html')

def logout1(request):
    logout(request)
    return HttpResponseRedirect('/login')














