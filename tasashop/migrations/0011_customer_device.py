# Generated by Django 3.1.6 on 2021-06-24 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasashop', '0010_auto_20210623_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='device',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
