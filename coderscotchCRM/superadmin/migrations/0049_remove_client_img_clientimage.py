# Generated by Django 5.0.6 on 2024-07-08 07:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0048_remove_lead_lead_files_leadfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='img',
        ),
        migrations.CreateModel(
            name='ClientImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='client_images/')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='superadmin.client')),
            ],
        ),
    ]
