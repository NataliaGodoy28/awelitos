# Generated by Django 4.0.5 on 2022-06-17 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_mandatoaportador_monto'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagosAportador',
            fields=[
                ('id_pago', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_transaccion', models.CharField(max_length=30)),
                ('fecha_pago', models.CharField(max_length=10)),
                ('monto', models.IntegerField()),
                ('id_aportador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
    ]