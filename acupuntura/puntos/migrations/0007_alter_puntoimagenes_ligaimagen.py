# Generated by Django 4.1.3 on 2023-06-22 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("puntos", "0006_alter_puntocaracteristicas_desccaracteristicas_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puntoimagenes",
            name="ligaimagen",
            field=models.ImageField(
                db_column="LigaImagen", max_length=255, upload_to="images_parameter"
            ),
        ),
    ]
