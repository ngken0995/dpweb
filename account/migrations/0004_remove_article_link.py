# Generated by Django 3.0.7 on 2020-08-13 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_article_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='link',
        ),
    ]