# Generated by Django 3.1.1 on 2020-11-09 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_card_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='text',
        ),
        migrations.AddField(
            model_name='card',
            name='warning',
            field=models.TextField(null=True),
        ),
    ]
