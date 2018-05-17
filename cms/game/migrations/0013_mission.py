# Generated by Django 2.0.3 on 2018-05-13 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20180513_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.SmallIntegerField()),
                ('state', models.SmallIntegerField()),
                ('times_completed', models.SmallIntegerField()),
                ('last_completion', models.IntegerField()),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Character')),
            ],
        ),
    ]