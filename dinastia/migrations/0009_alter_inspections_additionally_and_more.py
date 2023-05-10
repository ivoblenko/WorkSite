# Generated by Django 4.0.4 on 2022-05-08 13:04

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0008_alter_inspectionstemplates_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspections',
            name='additionally',
            field=tinymce.models.HTMLField(verbose_name='Дополнительно'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='anamnesis',
            field=tinymce.models.HTMLField(verbose_name='Анамнез'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='complaints',
            field=tinymce.models.HTMLField(verbose_name='Жалобы'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='diagnosis',
            field=tinymce.models.HTMLField(verbose_name='Диагноз'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinastia.patients', verbose_name='Пациент'),
        ),
        migrations.AlterField(
            model_name='inspections',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dinastia.staffs', verbose_name='Сотрудник'),
        ),
    ]