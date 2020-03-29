from django.shortcuts import render
from .models import NewsletterSubscription
from .serializers import NewsletterSubscriptionSerializers
from rest_framework import viewsets
from .forms import NewsletterSubscriptionForm


def index(request):
    if request.method == "POST":
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()

    form = NewsletterSubscriptionForm()

    return render(request, "home/index.htm", {"form": form})


class NewsletterSubscriptionView(viewsets.ModelViewSet):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializers
