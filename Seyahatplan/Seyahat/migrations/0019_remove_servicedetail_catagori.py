# Generated by Django 5.0.4 on 2024-05-05 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0018_servicedetail_catagori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetail',
            name='Catagori',
        ),
    ]
