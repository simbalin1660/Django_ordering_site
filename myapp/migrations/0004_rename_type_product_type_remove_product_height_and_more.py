# Generated by Django 4.1.7 on 2023-03-17 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='type',
            new_name='Type',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Length',
        ),
        migrations.RemoveField(
            model_name='product',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='ClosedWorkingHeight',
            field=models.CharField(choices=[('1', '350'), ('2', '400'), ('3', '450')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='WidthAndLength',
            field=models.CharField(choices=[('1', '1160x1680'), ('2', '1300x1985'), ('3', '1480x2113')], default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='mail',
            field=models.EmailField(max_length=200),
        ),
    ]
