# Generated by Django 5.1 on 2024-10-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='created at'),
        ),
    ]
