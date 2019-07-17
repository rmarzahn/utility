from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.conf.urls import url
from django.template import RequestContext
from django.http import HttpResponse
from .models import NewsletterUser, Newsletter
from .forms import NewsletterUserSignUpForm, NewsletterCreationForm

# Create your views here.

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 
            'Deine E-Mail existiert bereits in unserer Datenbank.', 
            "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, 
            'Vielen Dank für deine Registrierung zum Utility-Newsletter!', 
            'alert alert-success alert-dismissible')
            subject = "Dankeschön: Registrierung zum Utility-Newsletter!"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletter/templates/newsletter/sign_up_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/sign_up_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()

    context = {
        'form' : form,
    }
    template = "newsletter/nlsign_up.html"
    return render(request, template, context)



def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request, 
            'Deine E-Mail wurde entfernt.',
            "alert alert-success alert-dismissible")
            subject = "Abmeldung: Utility-Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/newsletter/templates/newsletter/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("newsletter/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        else:
            messages.warning(request, 
            'Deine E-Mail ist nicht in der Datenbank.', 
            "alert alert-warning alert-dismissible")            

    context = {
        'form':form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)



