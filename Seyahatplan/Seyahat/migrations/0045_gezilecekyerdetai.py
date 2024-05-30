# Generated by Django 5.0.4 on 2024-05-30 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0044_delete_gezilecekdetai'),
    ]

    operations = [
        migrations.CreateModel(
            name='gezilecekyerdetai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detai_title', models.CharField(max_length=50, null=True)),
                ('detai_GezilecekYer', models.CharField(max_length=200, unique=True)),
                ('detai_description', models.TextField()),
                ('detai_adresi', models.URLField(blank=True)),
                ('gezilecekyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='detaylar', to='Seyahat.gezilecekyer')),
            ],
        ),
    ]
