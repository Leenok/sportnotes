# Generated by Django 4.2.15 on 2024-08-11 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0006_approach_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='repeat',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
