# Generated by Django 4.0.2 on 2022-04-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zfitcoy', '0008_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='name',
        ),
    ]
