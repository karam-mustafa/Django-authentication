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


class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this

    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/google/login/callback/"
    client_class = OAuth2Client
    #Check if use active
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        print(self.request.data)
        try:
            self.serializer.is_valid(raise_exception=True)
        except Exception as e:
             return Response({"Failed": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        self.login()
        return self.get_response()

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

class Secure_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
       
    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)
