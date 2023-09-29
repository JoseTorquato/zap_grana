# Generated by Django 4.2.3 on 2023-09-29 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_remove_weddingregistration_street_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weddingregistration',
            options={'verbose_name_plural': 'Registros de Casamento'},
        ),
        migrations.AddField(
            model_name='weddingregistration',
            name='status',
            field=models.CharField(choices=[('reservado', 'Reservado'), ('ocupado', 'Ocupado')], default='reservado', max_length=10),
        ),
    ]
