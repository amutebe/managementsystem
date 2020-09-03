# Generated by Django 3.0.2 on 2020-08-14 13:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operations_9001', '0025_auto_20200814_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_providerassessment',
            name='date_today',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date created:'),
        ),
        migrations.AddField(
            model_name='mod9001_providerassessment',
            name='entered_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='providerentered', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-14082020199', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-14082020185', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_processtable',
            name='process_number',
            field=models.CharField(default='Comp-Pr-14082020150', max_length=200, primary_key=True, serialize=False, verbose_name='Process ID:'),
        ),
        migrations.AlterField(
            model_name='mod9001_providerassessment',
            name='emp_perfrev_no',
            field=models.CharField(default='Comp-EA-Q-14082020233', max_length=200, primary_key=True, serialize=False, verbose_name='Emp.Perf.Review.No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_qmsplanner',
            name='planner_number',
            field=models.CharField(default='Comp-QP-14082020127', max_length=200, primary_key=True, serialize=False, verbose_name='Planner no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingplanner',
            name='plan_number',
            field=models.CharField(default='Comp-TP-14082020129', max_length=200, primary_key=True, serialize=False, verbose_name='Plan no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_trainingregister',
            name='training_number',
            field=models.CharField(default='Comp-TR-14082020190', max_length=200, primary_key=True, serialize=False, verbose_name='Training no.:'),
        ),
    ]