# Generated by Django 5.0.6 on 2024-06-11 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0008_employee_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='project',
        ),
    ]
