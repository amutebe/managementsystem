# Generated by Django 3.0.2 on 2020-05-16 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0060_auto_20200516_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_risks',
            name='riskdescription',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='riskdescription', to='issues_9001.riskdesc', verbose_name='Risk Description:'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-16052020885', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-16052020562', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-16052020858', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-16052020504', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]