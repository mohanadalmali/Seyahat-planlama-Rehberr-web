# Generated by Django 5.0.4 on 2024-05-23 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seyahat', '0034_remove_gezilecekyer_gezilecekyer2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='gezilecekdetai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField()),
                ('link_title', models.CharField(blank=True, max_length=100)),
                ('link_url', models.URLField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='gezilecekyer',
            old_name='description_1',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='gezilecekyer',
            name='GezilecekYer1',
        ),
        migrations.AddField(
            model_name='gezilecekyer',
            name='GezilecekYer',
            field=models.CharField(default=2, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]