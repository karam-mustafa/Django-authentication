from django.conf import settings

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.microsoft.views import  MicrosoftGraphOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from dj_rest_auth.models import get_token_model
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.app_settings import create_token

from allauth.account.adapter import get_adapter

from django.utils import timezone
from dj_rest_auth import jwt_auth
class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this

    adapter_class = GoogleOAuth2Adapter
    # callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
  


class MSLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
    
    adapter_class = MicrosoftGraphOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/ms/login/callback/"
    client_class = OAuth2Client

   
class Secure_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
       
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

