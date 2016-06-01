# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 00:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('schema', jsonfield.fields.JSONField()),
                ('form', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('answers', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('questionnaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='django_jsf.Questionnaire')),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='django_jsf.Survey'),
        ),
    ]