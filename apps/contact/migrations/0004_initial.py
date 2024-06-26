# Generated by Django 4.2.11 on 2024-05-07 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0003_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('PERSON', 'person'), ('COMPANY', 'company')], default='PERSON', max_length=7, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('building_no', models.CharField(blank=True, max_length=8, null=True)),
                ('street', models.CharField(blank=True, max_length=64, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=8, null=True)),
                ('city', models.CharField(blank=True, max_length=16, null=True)),
                ('country', models.CharField(blank=True, max_length=16, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.CharField(max_length=16, null=True)),
            ],
        ),
    ]
