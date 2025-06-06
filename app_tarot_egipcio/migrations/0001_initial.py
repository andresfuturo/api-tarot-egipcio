# Generated by Django 5.2 on 2025-05-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartaEgipcia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('significado', models.TextField()),
                ('elemento', models.CharField(max_length=50)),
                ('planeta', models.CharField(max_length=50)),
                ('palabra_clave', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
