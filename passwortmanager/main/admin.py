from django.contrib import admin

# Register your models here.
from .models import Password, User

admin.site.register(Password)
admin.site.register(User)