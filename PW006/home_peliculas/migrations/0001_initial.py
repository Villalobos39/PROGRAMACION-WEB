# Generated by Django 3.1.7 on 2021-03-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Genero', models.CharField(max_length=30)),
                ('Estreno', models.CharField(max_length=30)),
                ('Comentario', models.CharField(max_length=100)),
            ],
        ),
    ]
