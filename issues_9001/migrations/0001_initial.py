# Generated by Django 3.0.2 on 2020-03-23 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='mod9001_issues',
            fields=[
                ('issue_number', models.CharField(default='TEGA-CT23032020509', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:')),
                ('analysis_date', models.DateField(verbose_name='Date of Analysis:')),
                ('context', models.CharField(choices=[('1', 'Internal Issues'), ('2', 'External Issues')], max_length=200)),
                ('internal_issues', models.CharField(choices=[('1', 'Organisational Culture'), ('2', 'Organisational Knowledge'), ('3', 'Company Values'), ('4', 'ICT Infrastructure'), ('5', 'Available Resources'), ('6', 'Organisational Structure'), ('7', 'Strength'), ('8', 'Weaknesses')], max_length=200)),
                ('external_issues', models.CharField(choices=[('1', 'Organisational Culture'), ('2', 'Organisational Knowledge'), ('3', 'Company Values'), ('4', 'ICT Infrastructure'), ('5', 'Available Resources'), ('6', 'Organisational Structure'), ('7', 'Strength'), ('8', 'Weaknesses')], max_length=200)),
                ('description', models.TextField(blank=True, help_text='Please give description if any', null=True, verbose_name='Description:')),
                ('mitigation', models.TextField(blank=True, help_text='Please give description if any', null=True, verbose_name='Mitigation Action:')),
                ('due', models.DateField(verbose_name='When:')),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyst', to=settings.AUTH_USER_MODEL, verbose_name='Lead Analyst:')),
                ('responsibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsibility', to=settings.AUTH_USER_MODEL, verbose_name='Responsibility:')),
            ],
        ),
        migrations.CreateModel(
            name='mod9001_interestedParties',
            fields=[
                ('ip_number', models.CharField(default='TEGA-IP23032020872', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:')),
                ('analysis_date', models.DateField(verbose_name='Date of Analysis:')),
                ('context', models.CharField(choices=[('1', 'Internal Issues'), ('2', 'External Issues')], max_length=200)),
                ('internal_issues', models.CharField(choices=[('1', 'Customers'), ('2', 'Regulators'), ('3', 'Hardware/Equipment Suppliers'), ('4', 'Traning providers'), ('5', 'Security providers'), ('6', 'Internet providers'), ('7', 'Insurance providers'), ('8', 'Auditors'), ('9', 'Certification bodies'), ('10', 'Inspectors'), ('11', 'Business partners'), ('12', 'Competitors'), ('13', 'Neighbourhood'), ('14', 'Local authorities'), ('15', 'Family')], max_length=200)),
                ('external_issues', models.CharField(choices=[('1', 'Customers'), ('2', 'Regulators'), ('3', 'Hardware/Equipment Suppliers'), ('4', 'Traning providers'), ('5', 'Security providers'), ('6', 'Internet providers'), ('7', 'Insurance providers'), ('8', 'Auditors'), ('9', 'Certification bodies'), ('10', 'Inspectors'), ('11', 'Business partners'), ('12', 'Competitors'), ('13', 'Neighbourhood'), ('14', 'Local authorities'), ('15', 'Family')], max_length=200)),
                ('description', models.TextField(blank=True, help_text='Please give description if any', null=True, verbose_name='Description:')),
                ('interestedparties', models.CharField(choices=[('1', 'Control'), ('2', 'Influence'), ('3', 'Influence and Control')], max_length=200)),
                ('priority', models.CharField(choices=[('1', 'P1'), ('2', 'P2'), ('3', 'P3')], max_length=200, verbose_name='Priority:')),
                ('actiontaken', models.CharField(choices=[('1', 'Customers'), ('2', 'Regulators'), ('3', 'Hardware/Equipment Suppliers'), ('4', 'Traning providers'), ('5', 'Security providers'), ('6', 'Internet providers'), ('7', 'Insurance providers'), ('8', 'Auditors'), ('9', 'Certification bodies'), ('10', 'Inspectors'), ('11', 'Business partners'), ('12', 'Competitors'), ('13', 'Neighbourhood'), ('14', 'Local authorities'), ('15', 'Family')], max_length=200, verbose_name='Action to Manage IP:')),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Lead Analyst:')),
            ],
        ),
    ]