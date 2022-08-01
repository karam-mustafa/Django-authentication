from django.db import router
from django.urls import path, include
from .views import *



urlpatterns = [
   path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/secure/', Secure_api.as_view(), name='secure'),
    path('auth/ms/', MSLogin.as_view(), name='ms'),
    ] 
