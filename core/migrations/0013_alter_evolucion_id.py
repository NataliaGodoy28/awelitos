# Generated by Django 4.0.5 on 2022-06-12 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucion',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
