#!/bin/bash
#Crear entorno virtual y descargar las librerias
python3 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
deactivate

#Crear Usuario y asignar permisos
groupadd --system webapps
useradd --system --gid webapps --home /var/www/python/acupuntura acupuntura
#useradd --system --gid webapps --home /var/www/python/Fiesta eventos

chown -R acupuntura:webapps /var/www/python/acupuntura

chmod +x gunicorn_acupuntura.bash
#usermod -m -d /var/www/python/acupuntura/ acupuntura

#Crear Base de datos

# Datos de conexión a la base de datos
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
echo "Ingrese la contraseña para la conexión a la base de datos:"

#Acupuntura
ACUPUNTURA_SQL_DATABASE="salud"
ACUPUNTURA_SQL_USER="acupuntura"
ACUPUNTURA_SQL_PASSWORD="acupunturadjango"

read -s DB_PASSWORD

SQL2="CREATE DATABASE IF NOT EXISTS $ACUPUNTURA_SQL_DATABASE;"
SQL2+="GRANT ALL PRIVILEGES ON $ACUPUNTURA_SQL_DATABASE.* TO '$ACUPUNTURA_SQL_USER'@'$DB_HOST' IDENTIFIED BY '$ACUPUNTURA_SQL_PASSWORD';"

echo "Bases de datos y usuarios creados correctamente."

mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "$SQL2" || exit 1

#Instalar supervisor

cp acupuntura.conf /etc/supervisor/conf.d/acupuntura.conf
#Actualizar supervisor
supervisorctl reread
supervisorctl update
supervisorctl status


#Configuracion de Nginx
cp nginx /etc/nginx/sites-available/acupuntura
#Activar sitio Nginx
ln -s /etc/nginx/sites-available/acupuntura /etc/nginx/sites-enabled/acupuntura
service nginx restart


