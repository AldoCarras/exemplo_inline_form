# Generated by Django 2.2 on 2020-07-12 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ex_inline_form', '0003_auto_20200711_2120'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefone',
            name='whatsapp',
        ),
    ]
