# Generated by Django 5.0.6 on 2024-07-31 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0066_alter_client_company_alter_lead_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
