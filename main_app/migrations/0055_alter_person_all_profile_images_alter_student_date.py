# Generated by Django 5.1.4 on 2025-02-04 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0054_alter_person_actions_alter_person_awards_and_honors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='all_profile_images',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 4, 15, 18, 57, 201348)),
        ),
    ]
