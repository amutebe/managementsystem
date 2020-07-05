# Generated by Django 3.0.2 on 2020-05-17 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0107_auto_20200517_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_number',
            field=models.CharField(default='TEGA18052020191', max_length=200, primary_key=True, serialize=False, verbose_name='Corrective action no.:'),
        ),
        migrations.AlterField(
            model_name='car',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Carstatus', verbose_name='CAR status:'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='employeeID',
            field=models.CharField(default='TEGA683', max_length=10, primary_key=True, serialize=False, verbose_name='Employee ID'),
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