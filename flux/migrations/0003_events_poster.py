# Generated by Django 3.2.9 on 2021-12-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flux', '0002_auto_20211223_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='poster',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media'),
        ),
    ]
