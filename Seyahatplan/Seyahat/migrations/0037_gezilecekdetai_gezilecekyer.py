# Generated by Django 5.0.4 on 2024-05-24 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0036_rename_link_title_servicic_link_title2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gezilecekdetai',
            name='gezilecekyer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Seyahat.gezilecekyer'),
            preserve_default=False,
        ),
    ]
