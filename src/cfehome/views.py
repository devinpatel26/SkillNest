from django.shortcuts import render

from emails.forms import EmailForm

from emails.models import Email, EmailVerificationEvent

def home_view(request):
    template_name = 'home.html'
    form = EmailForm(request.POST or None)
    print(request.POST)
    context = {
        'form': form,
        "message" : ""
    }
    if form.is_valid():
        email_val = form.cleaned_data.get("email")
        emailobj, created = Email.objects.get_or_create(email=email_val)
        obj = EmailVerificationEvent.objects.create(
            parent = emailobj, 
            email= email_val, 
            attempts=0
            ).save(
        )
        # obj = form.save()
        print(obj)
        context['form'] = EmailForm()
        context['message'] = "Success! Check your email for the confirmation link."
    else:
        print(form.errors)
    return render(request, template_name, context)
