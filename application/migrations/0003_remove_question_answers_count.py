# Generated by Django 3.0.2 on 2020-01-08 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200108_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers_count',
        ),
    ]
