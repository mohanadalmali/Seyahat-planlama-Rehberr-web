# Generated by Django 5.0.4 on 2024-05-24 09:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0038_remove_gezilecekdetai_gezilecekyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='gezilecekdetai',
            name='gezilecekyer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Seyahat.gezilecekyer'),
            preserve_default=False,
        ),
    ]