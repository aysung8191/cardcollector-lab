# Generated by Django 4.1.6 on 2023-02-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_cover_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='covers',
            field=models.ManyToManyField(to='main_app.cover'),
        ),
    ]
