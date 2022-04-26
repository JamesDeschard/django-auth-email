import threading

from django.contrib.sites.models import Site
from django.utils.encoding import force_bytes  
from django.utils.http import urlsafe_base64_encode  
from django.template.loader import render_to_string  
from django.core.mail import EmailMessage  

from login.registration_tools.token_generator import account_activation_token

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        threading.Thread.__init__(self)
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
    
    def run(self):
        msg = EmailMessage(self.subject, self.html_content, to=self.recipient_list)
        msg.send()


def send_confirmation_email(user, email, password):
    current_site = Site.objects.get_current() 
    mail_subject = 'Activation link has been sent to your email id'  
    message = render_to_string('acc_active_email.html', {  
        'user': user, 
        'password': password, 
        'domain': current_site.domain,  
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),  
        'token': account_activation_token.make_token(user),  
    })  

    EmailThread(mail_subject, message, [email]).start()
    return True