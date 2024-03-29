# Generated by Django 4.1.1 on 2022-09-17 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('documento', models.CharField(max_length=10)),
                ('nPersona', models.CharField(max_length=40)),
                ('nUsuario', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=254)),
                ('fechaCreacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
