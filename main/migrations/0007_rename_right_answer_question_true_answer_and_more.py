# Generated by Django 5.2 on 2025-04-19 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_test_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='right_answer',
            new_name='true_answer',
        ),
        migrations.AlterField(
            model_name='test',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 29, 10, 25, 14, 336812, tzinfo=datetime.timezone.utc)),
        ),
    ]
