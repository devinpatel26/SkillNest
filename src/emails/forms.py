from django import forms

from .css import EMAIL_FIELD_CSS
# from .models import Email, EmailVerificationEvent

from . import css


class EmailForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "id" : "email",
                "placeholder": "Your email",
                "class": css.EMAIL_FIELD_CSS
            }
        )
    )

    # class Meta:
    #     model = EmailVerificationEvent
    #     fields = ['email']


    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            raise forms.ValidationError("We do not accept gmail emails")
        return email
