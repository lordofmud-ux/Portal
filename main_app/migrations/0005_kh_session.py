# Generated by Django 3.1.1 on 2024-08-14 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20240814_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='kh',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.session'),
        ),
    ]
