# Generated by Django 4.0.3 on 2022-12-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0031_remove_product_extrafield_product_dayslimit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='extraField',
            field=models.CharField(max_length=232333332, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='adsType',
            field=models.CharField(max_length=232333332, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='expiry',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='plan',
            field=models.CharField(max_length=232333332, null=True),
        ),
    ]
