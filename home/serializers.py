from .models import NewsletterSubscription
from rest_framework import serializers


class NewsletterSubscriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = "__all__"
