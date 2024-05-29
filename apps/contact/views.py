from django.shortcuts import render
import datetime

from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from apps.contact.models import Contact
from apps.contact.serializers import ContactSerializer
from apps.outlook_service.connector import OutlookServiceConnector


# Create your views here.


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class OutlookViewSet(ViewSet):
    outlook_connector = OutlookServiceConnector()

    @action(detail=False, methods=['get'])
    def get_authorization_url(self, request, *args, **kwargs):
        response = self.outlook_connector.get_authorization_url()

        return Response(
            data=response.json(),
            status=response.status_code
        )
