# Generated by Django 5.0.6 on 2024-07-04 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0034_rename_company_superadmin_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employees',
            field=models.ManyToManyField(related_name='projects', to='superadmin.employee'),
        ),
    ]
