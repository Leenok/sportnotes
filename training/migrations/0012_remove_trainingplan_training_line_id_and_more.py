# Generated by Django 4.2.15 on 2024-08-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0011_trainingline_type_of_approaches_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingplan',
            name='training_line_id',
        ),
        migrations.AddField(
            model_name='trainingline',
            name='training_plan_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.trainingplan'),
        ),
    ]