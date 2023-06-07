#!/bin/bash

# Define las variables de entorno de Eventos
export EVENTOS_SQL_ENGINE="django.db.backends.mysql"
export EVENTOS_SQL_DATABASE="eventos"
export EVENTOS_SQL_USER="eventos"
export EVENTOS_SQL_PASSWORD="eventosdjango"
export EVENTOS_SQL_HOST="127.0.0.1"
export EVENTOS_SQL_PORT="3306"

# Define las variables de entorno de Acupuntura
export ACUPUNTURA_SQL_ENGINE="django.db.backends.mysql"
export ACUPUNTURA_SQL_DATABASE="salud"
export ACUPUNTURA_SQL_USER="acupuntura"
export ACUPUNTURA_SQL_PASSWORD="acupunturadjango"
export ACUPUNTURA_SQL_HOST="127.0.0.1"
export ACUPUNTURA_SQL_PORT="3306"

echo "Variables de entorno definidas correctamente."
