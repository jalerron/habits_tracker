# Generated by Django 5.0.2 on 2024-03-25 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='periodicity',
            field=models.CharField(choices=[('DAILY', 'Daily'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='DAILY', verbose_name='периодичность'),
        ),
    ]
