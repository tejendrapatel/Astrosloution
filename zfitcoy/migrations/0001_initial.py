# Generated by Django 3.2.4 on 2021-08-25 15:24

from django.db import migrations, models
import django.db.models.deletion
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', djrichtextfield.models.RichTextField(null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('categorys', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zfitcoy.blog_category')),
            ],
        ),
    ]
