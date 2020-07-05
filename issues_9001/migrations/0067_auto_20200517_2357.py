# Generated by Django 3.0.2 on 2020-05-17 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0066_auto_20200517_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_risks',
            name='residuelikelihood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='risklikelihood', to='issues_9001.residuerisklikelihood', verbose_name='Risk likelihood:'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mod9001_risks',
            name='residueriskrank',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Risk category:'),
        ),
        migrations.AddField(
            model_name='mod9001_risks',
            name='residueriskrating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Risk Rating:'),
        ),
        migrations.AddField(
            model_name='mod9001_risks',
            name='residueseverity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='riskseverity', to='issues_9001.residueriskseverity', verbose_name='Risk Severity:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-17052020149', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-17052020458', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-17052020115', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-17052020437', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]