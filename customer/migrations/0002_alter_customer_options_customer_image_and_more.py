# Generated by Django 5.0.6 on 2024-06-25 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['joined'], 'verbose_name_plural': 'Xaridorlar'},
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(default=2, upload_to='customers/custome_imag', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 25, 14, 34, 31, 425658), verbose_name='qo`shilgan vaqti'),
        ),
    ]
