from django.shortcuts import render
import datetime

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.contact.models import Contact
from apps.contact.serializers import ContactSerializer


# Create your views here.


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
