# Generated by Django 4.1.6 on 2023-02-05 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
