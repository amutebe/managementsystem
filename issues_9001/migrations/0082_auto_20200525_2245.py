# Generated by Django 3.0.2 on 2020-05-25 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0081_auto_20200525_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='process_OpportunitiesThreats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Process Opportunities/Threats')),
            ],
        ),
        migrations.CreateModel(
            name='process_StrengthWeakness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Process Strength/Weakness')),
            ],
        ),
        migrations.RemoveField(
            model_name='mod9001_issues',
            name='external_description',
        ),
        migrations.RemoveField(
            model_name='mod9001_issues',
            name='internal_description',
        ),
        migrations.RemoveField(
            model_name='mod9001_issues',
            name='process_description',
        ),
        migrations.AddField(
            model_name='mod9001_issues',
            name='otherIssue',
            field=models.TextField(blank=True, help_text='Please specify other', null=True, verbose_name='Other Issue:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-25052020474', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='external_issues',
            field=models.CharField(blank=True, choices=[('1', 'Legal and Regulatory requirements'), ('2', 'Economic enviroment'), ('3', 'Cultural enviroment'), ('4', 'Political enviroment'), ('5', 'Competitive enviroment'), ('6', 'Social enviroment'), ('7', 'Threats'), ('8', 'Opportunities'), ('9', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='internal_issues',
            field=models.CharField(blank=True, choices=[('1', 'Organisational Culture'), ('2', 'Organisational Knowledge'), ('3', 'Company Values'), ('4', 'ICT Infrastructure'), ('5', 'Available Resources'), ('6', 'Organisational Structure'), ('7', 'Strength'), ('8', 'Weaknesses'), ('9', 'Other')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-25052020227', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-25052020558', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-25052020236', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.DeleteModel(
            name='external_description',
        ),
        migrations.DeleteModel(
            name='internal_description',
        ),
        migrations.DeleteModel(
            name='process_description',
        ),
        migrations.AddField(
            model_name='mod9001_issues',
            name='process_OpportunitiesThreats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='process_OpportunitiesThreats', to='issues_9001.process_OpportunitiesThreats', verbose_name='Process Opportunities/Threats:'),
        ),
        migrations.AddField(
            model_name='mod9001_issues',
            name='process_StrengthWeakness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='process_StrengthWeakness', to='issues_9001.process_StrengthWeakness', verbose_name='process Strength/Weakness:'),
        ),
    ]
