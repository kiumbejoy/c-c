# Generated by Django 3.1.3 on 2021-01-02 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201231_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
