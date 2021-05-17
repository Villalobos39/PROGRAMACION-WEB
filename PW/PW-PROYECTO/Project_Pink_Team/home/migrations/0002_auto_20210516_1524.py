# Generated by Django 3.1.7 on 2021-05-16 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='regidter_update',
            new_name='register_update',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='telefono',
            new_name='telefono_casa',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_alumno',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='is_docente',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_nacimiento',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono_cel',
            field=models.CharField(default='default', max_length=32),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_de_usuario',
            field=models.CharField(choices=[('Alumno', 'Alumno'), ('Docente', 'Docente'), ('Administrador', 'Administrador'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20),
        ),
    ]
