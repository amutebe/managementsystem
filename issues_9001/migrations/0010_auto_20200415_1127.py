# Generated by Django 3.0.2 on 2020-04-15 08:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues_9001', '0009_auto_20200415_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP_Q-15042020809', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT_Q-15042020303', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP_LRO_Q-15042020373', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.CreateModel(
            name='mod9001_risks',
            fields=[
                ('risk_number', models.CharField(default='TEGA-RA-15042020682', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:')),
                ('risk_date', models.DateField(verbose_name='Date of analysis:')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Risk Description:')),
                ('mitigation', models.TextField(blank=True, help_text='Please give description if any', null=True, verbose_name='Mitigation Action:')),
                ('evidence', models.TextField(blank=True, null=True, verbose_name='Evidence of documented information:')),
                ('upload', models.FileField(upload_to='uploads/')),
                ('date_today', models.DateField(default=datetime.datetime.now, verbose_name='Date created:')),
                ('due', models.DateField(null=True, verbose_name='When:')),
                ('assessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Lead Assessor:')),
                ('contextdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contextdetail', to='issues_9001.contextdetails', verbose_name='Context:')),
                ('entered_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='risk_entered_by', to=settings.AUTH_USER_MODEL)),
                ('likelihood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='risklikelihood', to='issues_9001.risklikelihood', verbose_name='Risk likelihood:')),
                ('responsibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskresponsibility', to=settings.AUTH_USER_MODEL, verbose_name='Responsibility:')),
                ('severity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='riskseverity', to='issues_9001.riskseverity', verbose_name='Risk Severity:')),
            ],
        ),
    ]
