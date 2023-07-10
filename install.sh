#!/bin/bash
# Variables Acupuntura
export ACUPUNTURA_SQL_ENGINE="django.db.backends.mysql"
export ACUPUNTURA_SQL_DATABASE="salud"
export ACUPUNTURA_SQL_USER="acupuntura"
export ACUPUNTURA_SQL_PASSWORD="acupunturadjango"
export ACUPUNTURA_SQL_HOST="127.0.0.1"
export ACUPUNTURA_SQL_PORT="3306"

# Variables Acupuntura
export ACUPUNTURA_SQL_ENGINE
export ACUPUNTURA_SQL_DATABASE
export ACUPUNTURA_SQL_USER
export ACUPUNTURA_SQL_PASSWORD
export ACUPUNTURA_SQL_HOST
export ACUPUNTURA_SQL_PORT


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


#Crear entorno virtual y descargar las librerias
python3 -m venv virtual
source virtual/bin/activate

pip3 install -r requirements.txt
cd acupuntura
python3 manage.py migrate
python3 manage.py collectstatic
python3 mage.py loaddata puntos.json
python3 manage.py createsuperuser
cd ..
deactivate
mkdir logs
mkdir run

#Crear Usuario y asignar permisos
groupadd --system webapps
useradd --system --gid webapps --home /var/www/python/acupuntura acupuntura
#useradd --system --gid webapps --home /var/www/python/Fiesta eventos

chown -R acupuntura:webapps /var/www/python/acupuntura

chmod +x gunicorn_acupuntura.bash
#usermod -m -d /var/www/python/acupuntura/ acupuntura


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


