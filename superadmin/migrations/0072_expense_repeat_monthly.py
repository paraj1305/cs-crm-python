# Generated by Django 5.0.6 on 2024-08-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0071_alter_expense_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='repeat_monthly',
            field=models.BooleanField(default=False),
        ),
    ]
