# Generated by Django 4.0.4 on 2022-05-28 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0019_patients_contact_persan_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patients',
            old_name='stable_address',
            new_name='permanent_address',
        ),
        migrations.RenameField(
            model_name='patients',
            old_name='reg_address',
            new_name='registration_address',
        ),
    ]