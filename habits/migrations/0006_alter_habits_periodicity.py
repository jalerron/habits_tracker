# Generated by Django 5.0.2 on 2024-03-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_habits_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='periodicity',
            field=models.PositiveIntegerField(default=1, verbose_name='периодичность'),
        ),
    ]