# Generated by Django 5.0.6 on 2024-06-27 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0002_hotel_categoria_hotel_en_oferta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='porcentaje_descuento',
            field=models.IntegerField(default=0),
        ),
    ]
