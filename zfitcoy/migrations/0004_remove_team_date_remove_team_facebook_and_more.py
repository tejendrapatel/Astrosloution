# Generated by Django 4.0.2 on 2022-03-24 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zfitcoy', '0003_remove_contact_mobile_remove_contact_query'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='date',
        ),
        migrations.RemoveField(
            model_name='team',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='team',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='team',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='team',
            name='twitter',
        ),
        migrations.AlterField(
            model_name='team',
            name='detail',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
