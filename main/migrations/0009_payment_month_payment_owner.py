# Generated by Django 4.1.4 on 2022-12-23 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_teacher_first_name_teacher_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='month',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
