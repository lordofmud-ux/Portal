# Generated by Django 3.1.1 on 2024-11-23 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0026_auto_20241120_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ptro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(1, 'HOD'), (2, 'Staff'), (3, 'Sugar'), (4, 'Kh'), (5, 'Holding'), (6, 'Piran'), (7, 'Tomato'), (8, 'Taraghi'), (9, 'Tootia'), (10, 'Drug'), (11, 'Gen'), (12, 'Iron'), (13, 'Ptro')], default=1, max_length=1),
        ),
        migrations.CreateModel(
            name='PtroResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.FloatField(default=0)),
                ('exam', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ptro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ptro')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='ptro',
            name='admin',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ptro',
            name='organ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.organ'),
        ),
        migrations.AddField(
            model_name='ptro',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.session'),
        ),
        migrations.CreateModel(
            name='NotificationPtro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ptro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ptro')),
            ],
        ),
        migrations.CreateModel(
            name='LeaveReportPtro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=60)),
                ('message', models.TextField()),
                ('status', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ptro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ptro')),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackPtro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('reply', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ptro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.ptro')),
            ],
        ),
        migrations.AddField(
            model_name='attendancereport',
            name='ptro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main_app.ptro'),
        ),
    ]
