# Generated by Django 5.1.4 on 2025-02-05 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0074_alter_customuser_is_test_alter_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_test',
            field=models.BooleanField(choices=[('T', 'True'), ('F', 'False')], default='F'),
        ),
        migrations.AlterField(
            model_name='student',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 2, 5, 13, 7, 21, 537005)),
        ),
    ]
