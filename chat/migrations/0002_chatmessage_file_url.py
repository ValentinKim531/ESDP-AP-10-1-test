# Generated by Django 4.2.2 on 2023-07-14 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='file_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]