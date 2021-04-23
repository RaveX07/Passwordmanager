from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import PasswordForm

from .models import User
from .models import Password
# Create your views here.
def home_view(request, *args, **kwargs):
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

def create_new_password_view(request, *args, **kwargs):
    print(request.user)
    initial_D = {
        'user': str(request.user)
    }
    form = PasswordForm(initial=initial_D)
    form.fields['user'].widget.attrs['readonly'] = True
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PasswordForm(initial=initial_D)
        form.fields['user'].widget.attrs['readonly'] = True
    context = {
        'form': form
    }
    return render(request, "createNewPassword.html", context)

def delete_password(request, pk):
    password = get_object_or_404(Password, pk=pk)
    password.delete()
    return redirect('/')