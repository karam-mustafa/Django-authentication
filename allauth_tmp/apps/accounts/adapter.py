from django.utils.translation import gettext_lazy as _
from django import forms
from allauth.account.adapter import DefaultAccountAdapter


# User = get_user_model()
class MyCustomAdapter(DefaultAccountAdapter):
    custom_error_messages= {
         "not_active": _(
            "User is not active!"
        ),
    }
    error_messages = dict(list(DefaultAccountAdapter.error_messages.items()) + list(custom_error_messages.items()))
 

    def respond_user_inactive(self, request, user):
        raise forms.ValidationError(self.error_messages["not_active"])
