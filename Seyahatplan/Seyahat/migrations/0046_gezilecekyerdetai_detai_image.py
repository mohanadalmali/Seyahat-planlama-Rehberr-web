# Generated by Django 5.0.4 on 2024-05-30 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0045_gezilecekyerdetai'),
    ]

    operations = [
        migrations.AddField(
            model_name='gezilecekyerdetai',
            name='detai_image',
            field=models.ImageField(default=2, upload_to='media'),
            preserve_default=False,
        ),
    ]
