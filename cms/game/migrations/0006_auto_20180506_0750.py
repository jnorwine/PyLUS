# Generated by Django 2.0.3 on 2018-05-06 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20180504_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
