# Generated by Django 3.0.2 on 2020-03-23 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0040_auto_20200310_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_dateoccur',
            field=models.DateField(error_messages={'unique': 'The Geeks Field you enetered is not unique.'}, verbose_name='Date of Occurence:'),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA23032020915', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='car',
            name='deadline',
            field=models.DateField(verbose_name='Implementation Deadline:'),
        ),
        migrations.AlterField(
            model_name='car',
            name='proposedDate',
            field=models.DateField(verbose_name='CA/PA proposal Date:'),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Carstatus', verbose_name='CAR status:'),
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
