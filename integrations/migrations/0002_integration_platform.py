# Generated by Django 4.2.3 on 2023-08-06 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='integration',
            name='platform',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
