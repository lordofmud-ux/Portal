# Generated by Django 3.1.1 on 2024-09-03 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_auto_20240831_0805'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancereport',
            name='holding',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.holding'),
        ),
    ]
