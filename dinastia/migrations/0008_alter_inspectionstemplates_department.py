# Generated by Django 4.0.4 on 2022-05-07 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0007_inspectionstemplates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspectionstemplates',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinastia.departments', unique=True),
        ),
    ]