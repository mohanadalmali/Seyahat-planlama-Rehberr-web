# Generated by Django 5.0.4 on 2024-05-16 19:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0029_servicic_service_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicic',
            name='service_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicics', to='Seyahat.servicedetail'),
        ),
    ]