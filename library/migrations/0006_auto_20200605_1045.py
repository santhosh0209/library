# Generated by Django 3.0.7 on 2020-06-05 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20200605_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rack_no',
            field=models.IntegerField(null=True),
        ),
    ]
