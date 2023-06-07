#!/bin/bash

# Datos de conexión a la base de datos
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""

# Obtener la contraseña para la conexión
echo "Ingrese la contraseña para la conexión a la base de datos:"
read -s DB_PASSWORD
echo

# Comandos SQL para crear bases de datos y usuarios
SQL1="CREATE DATABASE IF NOT EXISTS $EVENTOS_SQL_DATABASE;"
SQL1+="GRANT ALL PRIVILEGES ON $DB_NAME1.* TO '$EVENTOS_SQL_USER'@'$DB_HOST' IDENTIFIED BY '$EVENTOS_SQL_PASSWORD';"

SQL2="CREATE DATABASE IF NOT EXISTS $ACUPUNTURA_SQL_DATABASE;"
SQL2+="GRANT ALL PRIVILEGES ON $ACUPUNTURA_SQL_USER.* TO '$DB_USER2'@'$DB_HOST' IDENTIFIED BY '$ACUPUNTURA_SQL_PASSWORD';"

# Ejecutar comandos SQL en la base de datos
mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "$SQL1" || exit 1
mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "$SQL2" || exit 1

# Mostrar mensaje de éxito
echo "Bases de datos y usuarios creados correctamente."
