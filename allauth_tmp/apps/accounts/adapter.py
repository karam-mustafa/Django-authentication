from django.utils.translation import gettext_lazy as _
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from .models import User
from allauth.socialaccount.models import EmailAddress
from django.core.exceptions import ValidationError
from django.conf import settings
class MyCustomAdapter(DefaultAccountAdapter):
    custom_error_messages= {
         "not_active": _(
            "User is not active!"
        ),
    }
    error_messages = dict(list(DefaultAccountAdapter.error_messages.items()) + list(custom_error_messages.items()))
 

    def respond_user_inactive(self, request, user):
        raise ValidationError(self.error_messages["not_active"])


class MyCustomSocialAdapter(DefaultSocialAccountAdapter):
    if settings.USER_FIRST:

        custom_error_messages= {
            "no_user": _(
                "User Does not exist!"
            ),
        }
        error_messages = dict(list(DefaultAccountAdapter.error_messages.items()) + list(custom_error_messages.items()))
    

        def pre_social_login(self, request, sociallogin):

            # # social account already exists, so this is just a login
            if sociallogin.is_existing:
                return

            # # some social logins don't have an email address
            if not sociallogin.email_addresses:
                return

            # find the first verified email that we get from this sociallogin
            verified_email = None
            for email in sociallogin.email_addresses:
                if email.verified:
                    verified_email = email
                    break

            # no verified emails found, nothing more to do
            if not verified_email:
                return

            try:
                existing_user = User.objects.get(email__iexact=email.email)
                existing_user.first_name=sociallogin.user.first_name
                existing_user.last_name=sociallogin.user.last_name
                existing_user.save()
            except User.DoesNotExist:
                raise ValidationError(self.error_messages["no_user"])

            # Creat email Addresses 
            if  sociallogin.email_addresses:
                new_email=EmailAddress(
                    user=existing_user,
                    email=sociallogin.account.extra_data['email'],
                    verified=sociallogin.account.extra_data['verified_email'],
                    primary=True
                )
                new_email.save()
            # Connect existing user to the logined social account
            sociallogin.connect(request, existing_user)
    else:
        pass
