# Generated by Django 5.0.6 on 2024-08-10 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
