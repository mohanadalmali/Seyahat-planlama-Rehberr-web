# Generated by Django 5.0.4 on 2024-05-16 19:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0028_servicic_servicedetail_adreslink1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicic',
            name='service_detail',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='servicics', to='Seyahat.servicedetail'),
        ),
    ]
