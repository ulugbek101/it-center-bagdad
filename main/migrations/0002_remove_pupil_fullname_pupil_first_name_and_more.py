# Generated by Django 4.1.4 on 2022-12-20 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pupil',
            name='fullname',
        ),
        migrations.AddField(
            model_name='pupil',
            name='first_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Ism'),
        ),
        migrations.AddField(
            model_name='pupil',
            name='last_name',
            field=models.CharField(max_length=200, null=True, verbose_name='Familiya'),
        ),
    ]
