# Generated by Django 5.0.4 on 2024-05-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0022_remove_services_link_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicedetail',
            name='link_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='link_title2',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='link_url',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='link_url2',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='main_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='servicedetail',
            name='main_title2',
            field=models.CharField(default='', max_length=200),
        ),
    ]