# Generated by Django 3.1.7 on 2021-03-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=30)),
                ('precio', models.CharField(max_length=30)),
                ('tienda', models.CharField(max_length=30)),
                ('Vence', models.CharField(max_length=10)),
            ],
        ),
    ]
