# Generated by Django 3.2.7 on 2021-09-25 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('descricao', models.TextField(verbose_name='Descricao')),
                ('horario_func', models.TextField(verbose_name='Horario de funcionamento')),
                ('idade_minima', models.IntegerField(verbose_name='Idade Mínima')),
            ],
        ),
    ]
