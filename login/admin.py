from django.contrib import admin
from .models import User, CreateNewUserProcedure, EmailMessage
from django.contrib import messages

class RegisterUser(admin.ModelAdmin):
    pass

class RegisterEmailMessages(admin.ModelAdmin):
    pass

class RegisterNewUser(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        super(RegisterNewUser, self).save_model(request, obj, form, change)
        obj.save()
        self.create_new_real_user(request, obj)
    
    def message_user(self, *args):
        pass

    def create_new_real_user(self, request, obj):
        status, message = obj.create_new_user()
        if status:
            messages.success(request, 'Email was successfully sent!')
            messages.success(request, message)
        else:
            messages.error(request, 'An error occured during the mailing process!')
            messages.error(request, message)
        obj.delete()

admin.site.register(CreateNewUserProcedure, RegisterNewUser)
admin.site.register(EmailMessage, RegisterEmailMessages)
admin.site.register(User, RegisterUser)