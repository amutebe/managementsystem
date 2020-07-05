# Generated by Django 3.0.2 on 2020-05-17 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0065_auto_20200517_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='residuerisklikelihood',
            fields=[
                ('likelihood_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Risk likelihood ID:')),
                ('likelihood_desc', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.CreateModel(
            name='residueriskseverity',
            fields=[
                ('riskseverity_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Risk Severity ID:')),
                ('riskseverity_desc', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-17052020116', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-1705202078', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-17052020582', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-17052020156', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]
