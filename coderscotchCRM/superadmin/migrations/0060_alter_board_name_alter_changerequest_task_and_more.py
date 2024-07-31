# Generated by Django 5.0.6 on 2024-07-31 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0059_alter_project_client_alter_salaryslip_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='changerequest',
            name='task',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='invoiceitem',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='lead',
            name='company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='project_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
