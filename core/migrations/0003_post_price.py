# Generated by Django 3.1.1 on 2020-11-05 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=4000),
            preserve_default=False,
        ),
    ]
