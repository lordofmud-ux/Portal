# Generated by Django 5.1.4 on 2025-02-04 11:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0058_alter_person_personal_number_alter_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personal_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 4, 15, 27, 37, 197885)),
        ),
    ]
