# Generated by Django 5.0.2 on 2024-03-25 04:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, max_length=100, null=True, verbose_name='место')),
                ('time', models.TimeField(default='12:00:00', verbose_name='время выполнения')),
                ('action', models.CharField(max_length=150, verbose_name='действие')),
                ('is_nice', models.BooleanField(default=False, verbose_name='признак приятности')),
                ('periodicity', models.PositiveIntegerField(default=1, verbose_name='периодичность')),
                ('reward', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('duration', models.PositiveIntegerField(blank=True, null=True, verbose_name='время выполнения')),
                ('is_public', models.BooleanField(default=False, verbose_name='признак публичности')),
                ('related_habits', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habits', verbose_name='привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
