# Generated by Django 3.0.8 on 2020-07-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recapp', '0003_review_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]