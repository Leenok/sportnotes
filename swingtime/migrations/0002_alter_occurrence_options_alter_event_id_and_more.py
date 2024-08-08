# Generated by Django 5.0.6 on 2024-08-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swingtime', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occurrence',
            options={'base_manager_name': 'objects', 'ordering': ('start_time', 'end_time'), 'verbose_name': 'occurrence', 'verbose_name_plural': 'occurrences'},
        ),
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eventtype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
