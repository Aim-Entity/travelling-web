from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 's2-full-name c-forms', "placeholder": "Name"}), label='')

    email = forms.CharField(widget=forms.EmailInput
                            (attrs={'class': 's2-email c-forms',
                                    "placeholder": "Your Email"
                                    }), label='')

    subject = forms.CharField(widget=forms.TextInput
                              (attrs={'class': 's2-subject c-forms',
                                      "placeholder": "Subject"
                                      }), label='')

    message = forms.CharField(widget=forms.Textarea
                              (attrs={'class': 's2-message c-forms',
                                      "placeholder": "Message"
                                      }), label='')

    class Meta:
        model = Contact
        fields = ("name", "email", "subject", "message")
