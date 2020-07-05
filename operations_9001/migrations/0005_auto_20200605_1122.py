# Generated by Django 3.0.2 on 2020-06-05 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations_9001', '0004_auto_20200604_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='maintenance_number',
            field=models.CharField(default='TEGA-M-05062020325', max_length=200, primary_key=True, serialize=False, verbose_name='Maintenance no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_calibration',
            name='calibration_number',
            field=models.CharField(default='TEGA-C-05062020774', max_length=200, primary_key=True, serialize=False, verbose_name='Calibration no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='document_number',
            field=models.CharField(default='TEGA-Q-05062020981', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:'),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='origin',
            field=models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='retention',
            field=models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mod9001_document_manager',
            name='status',
            field=models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200, null=True),
        ),
    ]