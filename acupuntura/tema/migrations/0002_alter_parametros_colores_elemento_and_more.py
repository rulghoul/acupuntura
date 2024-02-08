# Generated by Django 4.1.3 on 2023-12-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tema", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parametros_colores",
            name="elemento",
            field=models.CharField(
                choices=[
                    ("pleca", "Color de pleca"),
                    ("menu", "Color de menu"),
                    ("fondo", "Color de fondo"),
                ],
                db_column="elemento",
                default="pleca",
                max_length=50,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="parametros_imagenes",
            name="title",
            field=models.CharField(
                choices=[
                    ("logo", "Logo de pleca"),
                    ("bigLogo", "Logo de Login"),
                    ("fondo", "Background "),
                ],
                default="logo",
                max_length=60,
                unique=True,
            ),
        ),
    ]