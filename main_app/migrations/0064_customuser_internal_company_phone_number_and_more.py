# Generated by Django 5.1.4 on 2025-02-05 05:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0063_alter_student_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='internal_company_phone_number',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 5, 9, 26, 36, 954573)),
        ),
    ]
