# Generated by Django 3.2.6 on 2021-08-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(verbose_name='Дата-Время'),
        ),
    ]