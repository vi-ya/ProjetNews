from django.urls import path
from .views import contact, email_sent

urlpatterns = [

path("contact/", contact, name="contact"),
path("email/", email_sent, name="email_sent"),
]