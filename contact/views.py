from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from home.forms import NewsletterSubscriptionForm


def index(request):
    if request.method == "POST":
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()

    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

    contact = ContactForm()
    form = NewsletterSubscriptionForm()

    return render(request, "contact/index.htm",
                  {"form": form,
                   "contact": contact
                   })
