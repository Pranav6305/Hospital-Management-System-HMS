# Generated by Django 5.0.7 on 2024-10-13 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_remove_bookappointment_patient_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookappointment',
            old_name='patientid',
            new_name='patient_id',
        ),
    ]
