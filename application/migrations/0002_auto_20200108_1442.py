# Generated by Django 3.0.2 on 2020-01-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answers_count',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество вариантов ответов'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='text',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Правильный ответ'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
