# Generated by Django 3.1.1 on 2024-09-29 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20240929_0735'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='Organ',
        ),
        migrations.RenameField(
            model_name='holding',
            old_name='course',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='kh',
            old_name='course',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='piran',
            old_name='course',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='course',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='course',
            new_name='organ',
        ),
        migrations.RenameField(
            model_name='sugar',
            old_name='course',
            new_name='organ',
        ),
    ]
