from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str  
from django.utils.http import urlsafe_base64_decode
from django.views import View 

from login.registration_tools.token_generator import account_activation_token


class Activate(View):

    def get(self, request, *args, **kwargs):
        user = get_user_model() 
        uidb64 = kwargs.get('uidb64')
        token = kwargs.get('token')

        try:  
            uid = force_str(urlsafe_base64_decode(uidb64))  
            user = user.objects.get(pk=uid)  
        except(TypeError, ValueError, OverflowError, user.DoesNotExist):  
            user = None  

        if user is not None and account_activation_token.check_token(user, token):  
            user.is_active = True  
            user.is_first_connection = True
            user.save() 

            return HttpResponse(f"Thank you {user.username}, you're account is now active...")

        else:  
            return HttpResponse('Activation link is invalid!')