# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-03 12:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="title")),
                (
                    "description",
                    models.CharField(max_length=100, verbose_name="description"),
                ),
            ],
            options={
                "verbose_name": "event",
                "verbose_name_plural": "events",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="EventType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "abbr",
                    models.CharField(
                        max_length=4, unique=True, verbose_name="abbreviation"
                    ),
                ),
                ("label", models.CharField(max_length=50, verbose_name="label")),
            ],
            options={
                "verbose_name": "event type",
                "verbose_name_plural": "event types",
            },
        ),
        migrations.CreateModel(
            name="Note",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("note", models.TextField(verbose_name="note")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="created"),
                ),
                ("object_id", models.PositiveIntegerField(verbose_name="object id")),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contenttypes.ContentType",
                        verbose_name="content type",
                    ),
                ),
            ],
            options={
                "verbose_name": "note",
                "verbose_name_plural": "notes",
            },
        ),
        migrations.CreateModel(
            name="Occurrence",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_time", models.DateTimeField(verbose_name="start time")),
                ("end_time", models.DateTimeField(verbose_name="end time")),
                (
                    "event",
                    models.ForeignKey(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="swingtime.Event",
                        verbose_name="event",
                    ),
                ),
            ],
            options={
                "verbose_name": "occurrence",
                "verbose_name_plural": "occurrences",
                "ordering": ("start_time", "end_time"),
            },
        ),
        migrations.AddField(
            model_name="event",
            name="event_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="swingtime.EventType",
                verbose_name="event type",
            ),
        ),
    ]