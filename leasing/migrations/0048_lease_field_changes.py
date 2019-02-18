# Generated by Django 2.1.7 on 2019-02-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0047_planunit_plot_division_effective_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lease',
            name='arrangement_decision',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Arrangement decision'),
        ),
        migrations.AlterField(
            model_name='lease',
            name='transferable',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Transferable'),
        ),
    ]
