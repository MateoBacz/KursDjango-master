# Generated by Django 2.1.5 on 2019-02-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0004_auto_20190209_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
