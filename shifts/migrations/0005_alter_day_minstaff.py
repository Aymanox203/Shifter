# Generated by Django 4.1 on 2022-12-08 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0004_alter_arrangement_mindaysoff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='minStaff',
            field=models.IntegerField(default=2),
        ),
    ]
