# Generated by Django 4.0 on 2021-12-30 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
        ('app', '0004_pontoturistico_avaliacoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enderecos.endereco'),
            preserve_default=False,
        ),
    ]
