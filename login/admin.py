from django.contrib import admin
from .models import User, CreateNewUserProcedure

class RegisterUser(admin.ModelAdmin):
    pass

class RegisterNewUser(admin.ModelAdmin):
    pass

admin.site.register(CreateNewUserProcedure, RegisterNewUser)
admin.site.register(User, RegisterUser)