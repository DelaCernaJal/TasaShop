# Generated by Django 3.1.6 on 2021-06-24 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasashop', '0022_auto_20210624_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordertrans',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]