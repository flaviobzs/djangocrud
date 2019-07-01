# Generated by Django 2.2 on 2019-06-28 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('quantidade_integrantes', models.IntegerField()),
                ('descricao', models.CharField(max_length=250)),
                ('data_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('sobrenome', models.CharField(max_length=250)),
                ('data_nascimento', models.DateField()),
                ('idade', models.IntegerField()),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('fk_equipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_teste.Equipe')),
            ],
        ),
    ]