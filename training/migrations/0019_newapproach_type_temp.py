# Generated by Django 4.2.15 on 2024-08-24 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0018_newtraining_newtrainingline_newapproach'),
    ]

    operations = [
        migrations.AddField(
            model_name='newapproach',
            name='type_temp',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
