# Generated by Django 4.0.3 on 2022-12-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adsapi', '0034_alter_pricing_chatsupport_alter_pricing_dedicatedrm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricing',
            name='OrderID',
            field=models.CharField(max_length=1211, null=True),
        ),
    ]