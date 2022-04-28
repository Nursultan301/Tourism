from django import forms

from contact.models import Contact


class ContactForm(forms.ModelForm):
    """ Форма подписки по email """
    class Meta:
        model = Contact
        fields = ('email', )
        widget = {
            'email': forms.TextInput(attrs={"class": "form-control mr-3", "placeholder": "Ваш email"})
        }
        labels = {
            "email": ""
        }