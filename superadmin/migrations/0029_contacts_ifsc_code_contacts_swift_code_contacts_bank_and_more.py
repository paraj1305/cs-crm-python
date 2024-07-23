# Generated by Django 5.0.6 on 2024-07-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superadmin', '0028_invoice_tax_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='IFSC_CODE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='SWIFT_CODE',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='bank',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='bank_no',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo/'),
        ),
        migrations.AddField(
            model_name='contacts',
            name='website',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
