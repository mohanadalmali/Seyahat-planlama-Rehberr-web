# Generated by Django 5.0.4 on 2024-05-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websi', '0003_remove_indexpage_index_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpage',
            name='why_choose_us_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
