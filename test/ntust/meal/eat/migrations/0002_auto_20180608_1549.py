# Generated by Django 2.0.5 on 2018-06-08 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
