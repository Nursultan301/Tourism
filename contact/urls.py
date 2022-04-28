from django.urls import path

from contact.views import ContactCreateView

urlpatterns = [
    path("", ContactCreateView.as_view(), name='contact')
]