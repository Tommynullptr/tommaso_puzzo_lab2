# Generated by Django 4.2.2 on 2023-06-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='totalprice',
            field=models.FloatField(default=0),
        ),
    ]
