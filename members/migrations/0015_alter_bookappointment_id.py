# Generated by Django 5.0.7 on 2024-10-13 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_remove_bookappointment_appointment_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookappointment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
