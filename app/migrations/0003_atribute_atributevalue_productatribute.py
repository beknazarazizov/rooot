# Generated by Django 5.0.6 on 2024-06-25 02:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_title_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='AtributeValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_name', models.CharField(max_length=125)),
            ],
        ),
        migrations.CreateModel(
            name='ProductAtribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atribute')),
                ('atribute_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.atributevalue')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
    ]
