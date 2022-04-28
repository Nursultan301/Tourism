from django.shortcuts import render
from django.views.generic import CreateView

from contact.forms import ContactForm
from contact.models import Contact


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
