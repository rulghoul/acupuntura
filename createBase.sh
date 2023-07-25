#!/bin/bash

#Crear Base de datos

# Datos de conexión a la base de datos
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
echo "Ingrese la contraseña para la conexión a la base de datos:"


read -s DB_PASSWORD

SQL2="CREATE DATABASE IF NOT EXISTS $ACUPUNTURA_SQL_DATABASE;"
SQL2+="GRANT ALL PRIVILEGES ON $ACUPUNTURA_SQL_DATABASE.* TO '$ACUPUNTURA_SQL_USER'@'$DB_HOST' IDENTIFIED BY '$ACUPUNTURA_SQL_PASSWORD';"

echo "Bases de datos y usuarios creados correctamente."

mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "$SQL2" || exit 1