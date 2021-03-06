"""passwortmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    #path('deletePassword/', views.delete_password, name="deletePassword"),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.delete_password, name='deletePassword'),
    path('createPassword/', views.create_new_password_view, name='createNewPassword'),
    path('login/', auth_views.LoginView.as_view(), name='Login'),
    path('logout/', views.logout_view, name='LogOut'),
    path('register/', views.register_view)
]
