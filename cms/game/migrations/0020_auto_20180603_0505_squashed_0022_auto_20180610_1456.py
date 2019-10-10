# Generated by Django 2.2.4 on 2019-10-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    
    replaces = [('game', '0020_auto_20180603_0505'), ('game', '0021_session_character'), ('game', '0022_auto_20180610_1456')]

    dependencies = [
        ('game', '0019_auto_20180526_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='id',
            new_name='objid',
        ),
        migrations.RemoveField(
            model_name='account',
            name='front_character',
        ),
        migrations.RemoveField(
            model_name='character',
            name='slot',
        ),
        migrations.AddField(
            model_name='character',
            name='is_front',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='mission',
            name='progress',
            field=models.IntegerField(),
        ),
        migrations.AddField(
            model_name='session',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.Character'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='character',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Character'),
        ),
    ]
