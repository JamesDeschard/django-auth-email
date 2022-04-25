from django import forms  

class SignupForm(forms.Form):  
    username = forms.CharField(max_length=128)
    email = forms.EmailField(max_length=200, help_text='Required')    
