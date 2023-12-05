#!/bin/bash

# Obtener la ruta actual del script
CURRENT_DIR=$(pwd)

# Creacion de carpetas
mkdir -p logs
mkdir -p run

# Crear Usuario y asignar permisos
if ! getent group webapps > /dev/null; then
    groupadd --system webapps
fi
# Verificar si el usuario 'acupuntura' ya existe
if id "acupuntura" &>/dev/null; then
    echo "El usuario 'acupuntura' ya existe. Actualizando el directorio home."
    usermod --home "$CURRENT_DIR" acupuntura
else
    echo "Creando el usuario 'acupuntura'."
    useradd --system --gid webapps --home "$CURRENT_DIR" acupuntura
fi

chown -R acupuntura:webapps "$CURRENT_DIR"

# Dar permisos de ejecución al script de Gunicorn
chmod +x gunicorn_acupuntura.bash

# Crear copias temporales de los archivos de configuración
cp acupuntura.conf acupuntura.conf.tmp
cp nginx nginx.tmp

# Reemplazar el marcador {DIRECTORIO} en los archivos de configuración temporales
sed -i "s|{DIRECTORIO}|$CURRENT_DIR|g" acupuntura.conf.tmp
sed -i "s|{DIRECTORIO}|$CURRENT_DIR|g" nginx.tmp

# Instalar y configurar supervisor
#cp acupuntura.conf.tmp /etc/supervisor/conf.d/acupuntura.conf
supervisorctl reread
supervisorctl update
supervisorctl status

# Configuracion de Nginx
#cp nginx.tmp /etc/nginx/sites-available/acupuntura

# Activar sitio Nginx
#ln -sf /etc/nginx/sites-available/acupuntura /etc/nginx/sites-enabled/

# Eliminar archivos temporales
#rm acupuntura.conf.tmp nginx.tmp

#service nginx restart
