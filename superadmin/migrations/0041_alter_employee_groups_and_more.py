# Generated by Django 5.0.6 on 2024-07-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('superadmin', '0040_alter_employee_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(related_name='employee_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(related_name='employee_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='superadmin',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
