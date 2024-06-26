# Generated by Django 5.0.4 on 2024-05-04 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Seyahat', '0014_remove_services_catagori_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='catagori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
                ('show_on_homepage', models.BooleanField(default=False)),
                ('link_title', models.CharField(blank=True, max_length=100)),
                ('link_url', models.URLField(blank=True)),
                ('link_title2', models.CharField(blank=True, max_length=100)),
                ('link_url2', models.URLField(blank=True)),
                ('main_title', models.CharField(max_length=200)),
                ('Catagori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Seyahat.catagori')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Seyahat.services')),
            ],
        ),
    ]
