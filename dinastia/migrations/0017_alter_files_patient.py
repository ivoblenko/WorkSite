# Generated by Django 4.0.4 on 2022-05-21 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0016_remove_files_inspection_files_patient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinastia.patients'),
        ),
    ]
