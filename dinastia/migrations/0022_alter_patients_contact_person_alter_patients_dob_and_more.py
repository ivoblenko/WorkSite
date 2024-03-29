# Generated by Django 4.0.4 on 2022-05-28 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0021_rename_contact_persan_patients_contact_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='contact_person',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='patronymic',
            field=models.CharField(max_length=200, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='permanent_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='phone',
            field=models.PositiveBigIntegerField(blank=True, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='registration_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='sex',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='snils',
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='staffs',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dinastia.departments'),
        ),
    ]
