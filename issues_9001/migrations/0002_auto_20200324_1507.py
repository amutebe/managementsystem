# Generated by Django 3.0.2 on 2020-03-24 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues_9001', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestedParties',
            fields=[
                ('IP_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Interested party ID:')),
                ('IP_name', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.CreateModel(
            name='RequirementCategory',
            fields=[
                ('cat_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Category ID:')),
                ('cat_name', models.TextField(verbose_name='Description:')),
            ],
        ),
        migrations.AlterField(
            model_name='mod9001_interestedparties',
            name='ip_number',
            field=models.CharField(default='TEGA-IP_Q-2403202013', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_issues',
            name='issue_number',
            field=models.CharField(default='TEGA-CT_Q-24032020704', max_length=200, primary_key=True, serialize=False, verbose_name='Issue no.:'),
        ),
        migrations.CreateModel(
            name='mod9001_regulatoryReq',
            fields=[
                ('regulatory_number', models.CharField(default='TEGA-IP_LRO_Q-24032020287', max_length=200, primary_key=True, serialize=False, verbose_name='IP No.:')),
                ('registered', models.DateField(verbose_name='Date of registration:')),
                ('otherCategory', models.TextField(blank=True, null=True, verbose_name='Other category:')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Describe:')),
                ('document', models.TextField(blank=True, null=True, verbose_name='Document Stipulating the Requirment:')),
                ('deadline', models.DateField(verbose_name='Due date:')),
                ('otherInterestedParty', models.TextField(blank=True, null=True, verbose_name='Other interested party:')),
                ('analyst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Lead Analyst:')),
                ('cat_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RequirementCategory', to='issues_9001.RequirementCategory', verbose_name='Requirement Category ID:')),
                ('interestedparty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interestedparty', to='issues_9001.InterestedParties', verbose_name='Interested Party ID:')),
                ('responsibility', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsibilities', to=settings.AUTH_USER_MODEL, verbose_name='Responsibility:')),
            ],
        ),
    ]