# Generated by Django 4.2.15 on 2024-08-22 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0014_alter_trainingline_training_plan_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingline',
            name='training_plan_id',
        ),
    ]
