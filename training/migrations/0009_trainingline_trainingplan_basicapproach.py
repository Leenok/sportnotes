# Generated by Django 4.2.15 on 2024-08-22 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('training', '0008_alter_program_repeat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.exercise')),
                ('sportsmen_id', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('training_line_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.trainingline')),
            ],
        ),
        migrations.CreateModel(
            name='BasicApproach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('quantity', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('weight', models.FloatField(blank=True, default=None, null=True)),
                ('distance', models.FloatField(blank=True, default=None, null=True)),
                ('type_temp', models.CharField(blank=True, max_length=100)),
                ('time', models.FloatField(blank=True, default=None, null=True)),
                ('time_rest', models.FloatField(blank=True, default=None, null=True)),
                ('isCompleted', models.BooleanField(default=False)),
                ('programm_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='training.trainingline')),
            ],
        ),
    ]