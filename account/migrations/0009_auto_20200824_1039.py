# Generated by Django 3.0.7 on 2020-08-24 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_calorie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calorie',
            old_name='moderately_active',
            new_name='moderatelyActive',
        ),
    ]
