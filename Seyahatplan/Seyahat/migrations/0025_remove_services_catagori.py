# Generated by Django 5.0.4 on 2024-05-15 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0024_alter_servicedetail_link_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='Catagori',
        ),
    ]
