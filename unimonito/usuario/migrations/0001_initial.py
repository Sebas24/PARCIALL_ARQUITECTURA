# Generated by Django 2.0.3 on 2018-10-20 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('franquicias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(max_length=50)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cedula', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=50)),
                ('Fecha_contrato', models.CharField(max_length=50)),
                ('Salario', models.CharField(max_length=50)),
                ('Empleado', models.CharField(max_length=50)),
                ('Nombre', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('idFranquicia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='franquicias.Franquicias')),
            ],
        ),
    ]
