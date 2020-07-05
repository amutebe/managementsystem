# Generated by Django 3.0.2 on 2020-05-18 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0070_auto_20200518_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-1805202025', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-18052020195', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-18052020964', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='contextdetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contextdetail', to='issues_9001.contextdetails', verbose_name='Context:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='likelihood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risklikelihood', to='issues_9001.risklikelihood', verbose_name='Risk likelihood:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-18052020222', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='riskdescription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riskdescription', to='issues_9001.riskdesc', verbose_name='Risk Description:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='riskrating',
            field=models.IntegerField(blank=True, null=True, verbose_name='Risk Rating:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risktreatment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='risktreatment', to='issues_9001.risktreat', verbose_name='Risk Treatment:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='severity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='riskseverity', to='issues_9001.riskseverity', verbose_name='Risk Severity:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='issues_9001.approval_status', verbose_name='Status:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='verification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='issues_9001.RISK_OPPverification', verbose_name='Verification:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='verification_status',
            field=models.CharField(blank=True, choices=[('Closed', 'Close'), ('Rejected', 'Reject')], max_length=200, null=True),
        ),
    ]
