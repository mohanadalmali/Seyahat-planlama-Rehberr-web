# Generated by Django 5.0.4 on 2024-05-04 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0012_servicedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='description1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='main_title1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='main_title2',
        ),
        migrations.RemoveField(
            model_name='services',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='services',
            name='title2',
        ),
    ]