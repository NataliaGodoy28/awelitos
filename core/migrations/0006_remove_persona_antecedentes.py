# Generated by Django 4.0.5 on 2022-06-05 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_persona_antecedentes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='antecedentes',
        ),
    ]
