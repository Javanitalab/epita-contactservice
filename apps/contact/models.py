from django.db import models


# Create your models here.


class Contact(models.Model):
    PERSON = 'PERSON'
    COMPANY = 'COMPANY'

    TYPE = (
        (PERSON, 'person'),
        (COMPANY, 'company'),
    )

    type = models.CharField(max_length=7, choices=TYPE, default=PERSON, null=True)

    name = models.CharField(max_length=64, null=True, blank=True)

    building_no = models.CharField(max_length=8, null=True, blank=True)
    street = models.CharField(max_length=64, null=True, blank=True)
    postal_code = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=16, null=True, blank=True)
    country = models.CharField(max_length=16, null=True, blank=True)

    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=16, null=True)
