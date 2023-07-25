#!/bin/bash

#Crear entorno virtual y descargar las librerias
python3 -m venv virtual
source virtual/bin/activate

python3 variables.py

pip3 install -r requirements.txt
cd acupuntura
python3 manage.py migrate
python3 manage.py collectstatic
python3 mage.py loaddata puntos.json
python3 manage.py createsuperuser
cd ..
deactivate