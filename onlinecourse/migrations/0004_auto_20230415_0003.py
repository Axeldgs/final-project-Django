# Generated by Django 3.1.3 on 2023-04-15 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20230414_2345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='is_correct',
            new_name='validation',
        ),
    ]
