# Generated by Django 3.2.9 on 2021-12-19 14:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0019_auto_20211208_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boat',
            name='boat_docs',
            field=models.FileField(blank=True, null=True, upload_to='BoatDocuments/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
        migrations.AlterField(
            model_name='ship',
            name='ship_docs',
            field=models.FileField(blank=True, null=True, upload_to='ShipDocuments/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
