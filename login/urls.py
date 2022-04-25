from django.urls import path  
from .views import HomeView, ActivateUserView, Login, ChangePasswordView

urlpatterns = [  
    path('', HomeView.as_view(), name = 'home'),  
    path('login/', Login.as_view(), name='login'),
    path('change_password', ChangePasswordView.as_view(), name='change_password'),
    path('activate/<uidb64>/<token>/', ActivateUserView.as_view(), name='activate'), 
]  