# Generated by Django 5.1.1 on 2024-11-13 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_asset_borrowed_date_asset_returned_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.CharField(choices=[('NA', 'Not Available'), ('AV', 'Available'), ('IU', 'In Use')], default='NA', max_length=2),
        ),
    ]
