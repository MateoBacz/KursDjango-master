# Generated by Django 2.1.5 on 2019-02-09 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0003_auto_20190209_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='question',
            new_name='questions',
        ),
    ]
