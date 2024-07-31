# Generated by Django 5.0.6 on 2024-06-10 11:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0004_alter_project_employees'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
