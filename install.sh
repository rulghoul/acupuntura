#!/bin/bash

#Creacion de carpetas
mkdir logs
mkdir run

#Crear Usuario y asignar permisos
groupadd --system webapps
useradd --system --gid webapps --home /var/www/python/acupuntura acupuntura

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
#service nginx restart


