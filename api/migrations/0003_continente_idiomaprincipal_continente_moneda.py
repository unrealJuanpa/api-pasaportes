# Generated by Django 4.2.7 on 2023-11-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_continente_pais_pasaporte_persona_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='continente',
            name='idiomaprincipal',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='continente',
            name='moneda',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
