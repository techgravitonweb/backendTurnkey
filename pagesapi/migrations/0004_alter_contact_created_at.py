# Generated by Django 4.0.3 on 2022-12-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesapi', '0003_alter_contact_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.CharField(default='2022-12-29', max_length=150),
        ),
    ]
