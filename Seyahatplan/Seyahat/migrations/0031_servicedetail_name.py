# Generated by Django 5.0.4 on 2024-05-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0030_alter_servicic_service_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='name',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]