# Generated by Django 2.2 on 2020-07-12 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ex_inline_form', '0002_auto_20200711_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
