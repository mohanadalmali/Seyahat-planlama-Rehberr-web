# Generated by Django 5.0.4 on 2024-05-03 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0008_servicedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicedetail',
            name='description',
        ),
        migrations.RemoveField(
            model_name='servicedetail',
            name='image',
        ),
        migrations.RemoveField(
            model_name='servicedetail',
            name='title',
        ),
    ]
