from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes  
from django.utils.http import urlsafe_base64_encode  
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage  

from login.registration_tools.token_generator import account_activation_token


def send_confirmation_email(request, user, form, password):
    current_site = get_current_site(request)  
    mail_subject = 'Activation link has been sent to your email id'  
    message = render_to_string('acc_active_email.html', {  
        'user': user, 
        'password': password, 
        'domain': current_site.domain,  
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  
        'token': account_activation_token.make_token(user),  
    })  
    to_email = form.cleaned_data.get('email')  
    email = EmailMessage(  
                mail_subject, message, to=[to_email]  
    )  
    email.send()  