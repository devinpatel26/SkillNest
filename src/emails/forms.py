from django import forms

from .css import EMAIL_FIELD_CSS
# from .models import Email, EmailVerificationEvent
from .models import Email

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
        qs = Email.objects.filter(email=email, active=False)
        if qs.exists():
            raise forms.ValidationError("Invalid email! Please verify your email.")
        return email
