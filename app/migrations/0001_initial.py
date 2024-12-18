# Generated by Django 5.1.2 on 2024-10-15 06:54

import banjo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', banjo.models.StringField(default='')),
                ('position', banjo.models.StringField(default='')),
                ('points', banjo.models.IntegerField(default=0)),
                ('rebounds', banjo.models.IntegerField(default=0)),
                ('assists', banjo.models.IntegerField(default=0)),
                ('blocks', banjo.models.IntegerField(default=0)),
                ('steals', banjo.models.IntegerField(default=0)),
                ('shotstaken', banjo.models.IntegerField(default=0)),
                ('shotsmade', banjo.models.IntegerField(default=0)),
                ('threestaken', banjo.models.IntegerField(default=0)),
                ('threesmade', banjo.models.IntegerField(default=0)),
                ('matchesplayed', banjo.models.IntegerField(default=0)),
                ('plusminus', banjo.models.IntegerField(default=0)),
                ('mvp', banjo.models.IntegerField(default=0)),
                ('active', banjo.models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
