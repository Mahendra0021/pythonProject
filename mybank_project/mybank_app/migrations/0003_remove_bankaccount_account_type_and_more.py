# Generated by Django 5.0 on 2023-12-28 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybank_app', '0002_bankaccount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='digital_picture',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='email_address',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='id_proof',
        ),
    ]
