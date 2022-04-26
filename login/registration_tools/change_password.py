from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.views import View 

class ChangePassword(View):
    template_name = ''

    def get(self, request, *args, **kwargs):
        context = {
            'form': PasswordChangeForm(request.user)
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        user = request.user
        form = PasswordChangeForm(user, request.POST)

        if form.is_valid():
            if user.is_first_connection is True:
                user.is_first_connection = False
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')

        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'registration/change_password.html', {'form': form})