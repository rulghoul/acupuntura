from django.core.management.base import BaseCommand
import csv
import os
from puntos.models import Elementos, CategoriaElemento, ValoresElemento, TablaElemento

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos desde un archivo CSV'

    def handle(self, *args, **kwargs):
        def get_or_create(model, **kwargs):
            instance, created = model.objects.get_or_create(**kwargs)
            return instance
        current_script_path = os.path.dirname(os.path.abspath(__file__))
        csv_file_path = os.path.join(current_script_path,  'importar.csv')
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tipo_punto = get_or_create(Elementos, nombre=row['TipoPunto'])
                categoria = get_or_create(CategoriaElemento, nombre=row['Categoria'])
                valor = get_or_create(ValoresElemento, nombre=row['Valores'])
                TablaElemento.objects.get_or_create(tipo=tipo_punto, categoria=categoria, valor=valor)

        self.stdout.write(self.style.SUCCESS('Base de datos poblada exitosamente'))
