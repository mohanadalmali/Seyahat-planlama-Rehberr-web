# Generated by Django 5.0.4 on 2024-05-29 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websi', '0007_alter_contactmessage_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
