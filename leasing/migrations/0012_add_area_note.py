# Generated by Django 2.0.6 on 2018-06-07 06:02

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leasing', '0011_add_view_lease_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time created')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Time modified')),
                ('geometry', django.contrib.gis.db.models.fields.MultiPolygonField(blank=True, null=True, srid=4326)),
                ('note', models.TextField(blank=True, null=True, verbose_name='Note')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]