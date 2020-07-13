# Generated by Django 3.0.2 on 2020-07-08 12:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations_9001', '0016_auto_20200625_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='noteffective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Reason not effective')),
            ],
        ),
        migrations.AddField(
            model_name='mod9001_trainingregister',
            name='date_today',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date created:'),
        ),
        migrations.AddField(
            model_name='mod9001_trainingregister',
            name='entered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='training_entered_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mod9001_trainingregister',
            name='reasonother',
            field=models.TextField(blank=True, null=True, verbose_name='If Not Effective, reason'),
        ),
        migrations.AddField(
            model_name='mod9001_trainingregister',
            name='train_date',
            field=models.DateField(null=True, verbose_name='Training Date:'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-08072020947', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-08072020705', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-0807202072', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-0807202012', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='decision',
            field=models.CharField(choices=[('1', 'Effective'), ('2', 'Not Effective')], max_length=200, null=True, verbose_name='Evaluation Decision:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-08072020408', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
        migrations.AddField(
            model_name='mod9001_trainingregister',
            name='reason',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='noteffectreason', to='operations_9001.noteffective', verbose_name='If Not Effective, other reason:'),
        ),
    ]
