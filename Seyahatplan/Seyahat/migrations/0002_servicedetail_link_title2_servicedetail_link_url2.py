# Generated by Django 5.0.4 on 2024-05-01 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='link_title2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='link_url2',
            field=models.URLField(blank=True),
        ),
    ]