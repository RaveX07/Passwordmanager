from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

from .forms import PasswordForm, RegisterForm

from .models import User
from .models import Password
# Create your views here.
def home_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user)

        Userlist = []
        PassworList = []

        for x in User.objects.all():
            Userlist.append(x)
        for y in Password.objects.all():
            PassworList.append(y)
        ctx = {
            'Userlist': Userlist,
            'Passwordlist': PassworList,
            'User': str(request.user),
        }
        return render(request, "home.html", ctx)
    else:
        return redirect("login/")

def create_new_password_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        print(request.user)
        initial_D = {
            'Benutzer': str(request.user)
        }
        form = PasswordForm(initial=initial_D)
        form.fields['Benutzer'].widget.attrs['readonly'] = True
        if request.method == 'POST':
            form = PasswordForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        else:
            form = PasswordForm(initial=initial_D)
            form.fields['Benutzer'].widget.attrs['readonly'] = True
        context = {
            'form': form
        }
        return render(request, "createNewPassword.html", context)
    else:
        return redirect("login/")

def delete_password(request, pk):
    password = get_object_or_404(Password, pk=pk)
    password.delete()
    return redirect('/')

def logout_view(request):
    logout(request)
    return redirect('/login/')

def register_view(request):
    if not request.user.is_authenticated:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm()
            if form.is_valid():
                form.save()
        else:
            form = UserCreationForm()
        return render(request, 'register.html', context={
            'form': form
        })
    return redirect("/")