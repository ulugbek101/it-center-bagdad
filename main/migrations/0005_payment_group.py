# Generated by Django 4.1.4 on 2022-12-20 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_payment_created_alter_payment_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.group'),
        ),
    ]
