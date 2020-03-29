from django import forms
from .models import NewsletterSubscription


class NewsletterSubscriptionForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'full_name-form', "placeholder": "Full Name"}), label='')

    e_mail = forms.CharField(widget=forms.TextInput
                             (attrs={'class': 'e_mail-form',
                                     "placeholder": "E-Mail"
                                     }), label='')

    class Meta:
        model = NewsletterSubscription
        fields = ("full_name", "e_mail")
