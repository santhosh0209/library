# Generated by Django 3.0.7 on 2020-06-05 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rack_no',
            field=models.CharField(default=None, max_length=5),
        ),
    ]
