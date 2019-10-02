# Generated by Django 2.2.5 on 2019-10-02 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leasing', '0072_tenantrentshare'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementSubventionFormOfManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Form of management (Subvention)',
                'verbose_name_plural': 'Form of management (Subvention)',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='leasebasisofrentmanagementsubvention',
            options={'verbose_name': 'Management subvention (Basis of rent)', 'verbose_name_plural': 'Management subventions (Basis of rent)'},
        ),
        migrations.AlterModelOptions(
            name='leasebasisofrenttemporarysubvention',
            options={'verbose_name': 'Temporary subvention (Basis of rent)', 'verbose_name_plural': 'Temporary subventions (Basis of rent)'},
        ),
        migrations.AlterModelOptions(
            name='managementsubvention',
            options={'verbose_name': 'Management subvention (Rent adjustment)', 'verbose_name_plural': 'Management subventions (Rent adjustment)'},
        ),
        migrations.AlterModelOptions(
            name='temporarysubvention',
            options={'verbose_name': 'Temporary subvention (Rent adjustment)', 'verbose_name_plural': 'Temporary subventions (Rent adjustment)'},
        ),
        migrations.RemoveField(
            model_name='leasebasisofrentmanagementsubvention',
            name='subvention_percent',
        ),
        migrations.RemoveField(
            model_name='managementsubvention',
            name='subvention_percent',
        ),
        migrations.AddField(
            model_name='leasebasisofrentmanagementsubvention',
            name='subvention_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subvention amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='managementsubvention',
            name='subvention_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Subvention amount'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leasebasisofrentmanagementsubvention',
            name='management',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='leasing.ManagementSubventionFormOfManagement', verbose_name='Form of management'),
        ),
        migrations.AlterField(
            model_name='managementsubvention',
            name='management',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='leasing.ManagementSubventionFormOfManagement', verbose_name='Form of management'),
        ),
    ]