import random
import string

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

from login.models import User
from login.forms import SignupForm
from login.registration_tools.email import send_confirmation_email

class HomeAndSignupView(View):
    template_name = ''

    def create_random_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(8))
        return password
    
    def get(self, request, *args, **kwargs):
        context = {
            'form': SignupForm() 
        }
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST) 

        if form.is_valid():   
            username, email = form.cleaned_data['username'], form.cleaned_data['email']
            password = self.create_random_password()   
            user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password) 
            user.is_active = False  
            user.save()  

            send_confirmation_email(request, user, form, password)

            return HttpResponse('Please confirm your email address to complete the registration')  