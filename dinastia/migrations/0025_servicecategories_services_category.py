# Generated by Django 4.0.4 on 2022-09-03 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dinastia', '0024_alter_services_external'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование')),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dinastia.servicecategories', verbose_name='Категория'),
            preserve_default=False,
        ),
    ]
