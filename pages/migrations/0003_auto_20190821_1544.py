# Generated by Django 2.1.5 on 2019-08-21 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20190821_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
