from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import EmailForm
from django_htmx.http import HttpResponseClientRedirect



from django.http import HttpResponse
from . import services as email_services
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def logout_btn_hx_view(request, *args, **kwargs):
    if not request.htmx:
        return redirect("/")
    if request.method == "POST":
        try:
            del request.session['email_id']
        except KeyError:
            pass
    email_id_in_session = request.session.get('email_id')
    if email_id_in_session:
        return render(request, "emails/hx/logout_btn.html", {})
    else:
        return HttpResponseClientRedirect("/")
    return render(request, "emails/hx/logout_btn.html", {})
        

def email_token_login_view(request, *args, **kwargs):
    if not request.htmx:
        return redirect("/")
    email_id_in_session = request.session.get('email_id')
    template_name = 'emails/hx/email_form.html'
    form = EmailForm(request.POST or None)
    context = {
        'form': form,
        "message": "",
        "show_form": not email_id_in_session
    }
    if form.is_valid():
        email_val = form.cleaned_data.get("email")
        obj = email_services.start_verification_event(email_val)
        context['form'] = EmailForm()  # Reset the form after successful submission
        context['message'] = "Success! Check your email for the confirmation link."
    else:
        print("Form Errors:", form.errors)  # Debugging: Print form errors
    print("email_id" , request.session.get('email_id'))  # Debugging: Print the session email_id
    return render(request, template_name, context)


def verify_email_token_view(request, token, *args, **kwargs):
    did_verify, msg, email = email_services.verify_token(token)
    if not did_verify:
        try:
            del request.session['email_id']
        except KeyError:
            pass
        messages.error(request, f"Failed to verify token: {msg}")
        return redirect("/login/")
    messages.success(request, msg)
    # Save the email ID in the session
    request.session['email_id'] = f"{email.id}"
    # Fetch next_url or default to /
    next_url = request.session.get("next_url") or "/"
    # Redirect to /courses/ if next_url is not a valid relative URL
    if not next_url.startswith("/"):
        next_url = "/"
    return redirect(next_url)
