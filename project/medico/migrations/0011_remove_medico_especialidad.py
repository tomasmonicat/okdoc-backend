# Generated by Django 4.2.3 on 2023-09-22 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0010_obrasocial_alter_relmedicoespecialidad_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='especialidad',
        ),
    ]
