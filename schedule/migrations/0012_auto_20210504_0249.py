# Generated by Django 3.2 on 2021-05-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0011_auto_20210504_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='area',
            field=models.CharField(max_length=100, verbose_name='場所'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='content',
            field=models.CharField(max_length=100, verbose_name='内容'),
        ),
    ]
