# Generated by Django 3.0.8 on 2020-07-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signapp', '0003_auto_20200717_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sofo_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='sofo 닉네임'),
        ),
    ]