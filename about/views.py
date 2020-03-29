from django.shortcuts import render
from home.serializers import NewsletterSubscriptionSerializers
from rest_framework import viewsets
from home.forms import NewsletterSubscriptionForm


def index(request):
    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

    form = NewsletterSubscriptionForm()

    return render(request, "about/index.htm", {"form": form})
