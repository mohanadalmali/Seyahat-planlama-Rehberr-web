# Generated by Django 5.0.4 on 2024-05-04 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0015_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='Catagori',
        ),
        migrations.RemoveField(
            model_name='servicedetail',
            name='service',
        ),
        migrations.DeleteModel(
            name='catagori',
        ),
        migrations.DeleteModel(
            name='ServiceDetail',
        ),
        migrations.DeleteModel(
            name='services',
        ),
    ]
