# Generated by Django 5.0.6 on 2024-08-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_program_count_approach'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approach',
            name='isCompleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='approach',
            name='quantity',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='approach',
            name='time',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='approach',
            name='time_rest',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='approach',
            name='weight',
            field=models.FloatField(default=None),
        ),
    ]
