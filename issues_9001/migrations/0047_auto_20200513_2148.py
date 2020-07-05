# Generated by Django 3.0.2 on 2020-05-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_9001', '0046_auto_20200513_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='mod9001_interestedparties',
            name='actionOther',
            field=models.TextField(blank=True, null=True, verbose_name='Other, specify'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='actiontaken',
            field=models.CharField(choices=[('1', 'Training and awareness'), ('2', 'Customer satisfaction survey'), ('3', 'Performance monitoring'), ('4', 'Service Level Management'), ('5', 'Tax Compliance/Policing'), ('6', 'Auditing'), ('7', 'Contract management'), ('8', 'Compliance reviews'), ('9', 'Others')], max_length=200, verbose_name='Action to Manage IP:'),
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP-Q-13052020601', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT-Q-13052020481', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_regulatoryreq',
            name='regulatory_number',
            field=models.CharField(default='TEGA-IP-LRO-Q-13052020687', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_risks',
            name='risk_number',
            field=models.CharField(default='TEGA-RA-13052020453', max_length=200, primary_key=True, serialize=False, verbose_name='RISK No.:'),
        ),
    ]
