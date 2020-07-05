# Generated by Django 3.0.2 on 2020-01-30 09:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0015_auto_20200127_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date created:'),
        ),
        migrations.AddField(
            model_name='car',
            name='correctiveaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.CorrectivePreventiveAction', verbose_name='Corrective/Preventive Action'),
        ),
        migrations.AddField(
            model_name='car',
            name='deadline',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Implementation Deadline:'),
        ),
        migrations.AddField(
            model_name='car',
            name='implementedby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='implementedby_user', to=settings.AUTH_USER_MODEL, verbose_name='Implemented by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='proposedby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='proposedby_user', to=settings.AUTH_USER_MODEL, verbose_name='Proposed by'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='rootcause',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.RootCause', verbose_name='Root Cause Analysis'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='300120202505', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='carstatus',
            name='car_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.car', verbose_name='CAR ID'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='accounts.Tag'),
        ),
    ]
