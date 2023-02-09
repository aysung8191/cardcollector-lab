# Generated by Django 4.1.6 on 2023-02-08 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('T', 'Top Loader'), ('O', 'One Touch'), ('G', 'Graded')], default='T', max_length=1)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cleaning',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='date',
            field=models.DateField(verbose_name='cleaning date'),
        ),
    ]
