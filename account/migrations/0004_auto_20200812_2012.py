# Generated by Django 3.1 on 2020-08-12 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200812_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statistic',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
