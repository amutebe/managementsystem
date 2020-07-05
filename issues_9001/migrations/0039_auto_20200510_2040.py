# Generated by Django 3.0.2 on 2020-05-10 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0038_auto_20200510_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='context',
            field=models.CharField(choices=[('1', 'Internal IP'), ('2', 'External IP')], max_length=200),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-10052020172', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-1005202055', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO_Q-10052020771', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-10052020114', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]