# Generated by Django 3.0.2 on 2020-05-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0062_auto_20200517_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mod9001_risks',
            name='likelihood_residue',
        ),
        migrations.RemoveField(
            model_name='mod9001_risks',
            name='riskrank_residue',
        ),
        migrations.RemoveField(
            model_name='mod9001_risks',
            name='riskrating_residue',
        ),
        migrations.RemoveField(
            model_name='mod9001_risks',
            name='severity_residue',
        ),
        migrations.AddField(
            model_name='mod9001_risks',
            name='mitigationdesc',
            field=models.TextField(blank=True, help_text='Please give risk mitigation details', null=True, verbose_name='Please describe if any:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-1705202011', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-17052020526', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-17052020227', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-17052020744', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]