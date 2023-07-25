#!/bin/bash

# Variables Acupuntura
export ACUPUNTURA_SQL_ENGINE="django.db.backends.mysql"
export ACUPUNTURA_SQL_DATABASE="salud"
export ACUPUNTURA_SQL_USER="acupuntura"
export ACUPUNTURA_SQL_PASSWORD="acupunturadjango"
export ACUPUNTURA_SQL_HOST="127.0.0.1"
export ACUPUNTURA_SQL_PORT="3306"


#Crear entorno virtual y descargar las librerias
python3 -m venv virtual
source virtual/bin/activate

# Variables Acupuntura
export ACUPUNTURA_SQL_ENGINE
export ACUPUNTURA_SQL_DATABASE
export ACUPUNTURA_SQL_USER
export ACUPUNTURA_SQL_PASSWORD
export ACUPUNTURA_SQL_HOST
export ACUPUNTURA_SQL_PORT

python3 variables.py

pip3 install -r requirements.txt
cd acupuntura
python3 manage.py migrate
python3 manage.py collectstatic
python3 mage.py loaddata puntos.json
python3 manage.py createsuperuser
cd ..
deactivate