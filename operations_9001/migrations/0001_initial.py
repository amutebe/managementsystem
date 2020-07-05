# Generated by Django 3.0.2 on 2020-06-02 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0126_auto_20200602_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='document_format',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Document format')),
            ],
        ),
        migrations.CreateModel(
            name='document_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Document location')),
            ],
        ),
        migrations.CreateModel(
            name='document_standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Standard')),
            ],
        ),
        migrations.CreateModel(
            name='document_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=50, null=True, verbose_name='Document type')),
            ],
        ),
        migrations.CreateModel(
            name='mod9001_document_manager',
            fields=[
                ('document_date', models.DateField(verbose_name='Date:')),
                ('document_number', models.CharField(default='TEGA-Q-02062020650', max_length=200, primary_key=True, serialize=False, verbose_name='Document no.:')),
                ('origin', models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200)),
                ('document_id', models.TextField(blank=True, help_text='Document ID', null=True, verbose_name='Document ID:')),
                ('clause', models.TextField(blank=True, help_text='Document ID', null=True, verbose_name='Document ID:')),
                ('version', models.TextField(blank=True, help_text='Version', null=True, verbose_name='Version No:')),
                ('retention', models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200)),
                ('status', models.CharField(choices=[('1', 'Interna'), ('2', 'External')], max_length=200)),
                ('document', models.FileField(blank=True, null=True, upload_to='uploads/', verbose_name='Please upload relevant document')),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='operations_9001.document_type', verbose_name='Document Type:')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='format', to='operations_9001.document_format', verbose_name='Format:')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='operations_9001.document_location', verbose_name='Location:')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='accounts.employees', verbose_name='Owner:')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='standard', to='operations_9001.document_standard', verbose_name='Standard:')),
            ],
        ),
    ]
