# Generated by Django 4.2.3 on 2023-08-09 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0002_integration_platform'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalledWebHook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('response_data', models.JSONField()),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.integration')),
            ],
        ),
    ]
