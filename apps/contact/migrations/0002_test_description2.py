# Generated by Django 4.2.11 on 2024-05-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='description2',
            field=models.TextField(null=True),
        ),
    ]
