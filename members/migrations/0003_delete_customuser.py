# Generated by Django 5.1.1 on 2024-10-09 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_customuser_delete_account'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
