#!/bin/bash
DIRECTORIO=$(pwd)
NAME="acupuntura"                                  # Name of the application
DJANGODIR=$DIRECTORIO/acupuntura            # Django project directory
SOCKFILE=$DIRECTORIO/run/gunicorn.sock  # we will communicte using this unix socket
USER=acupuntura                                        # the user to run as
GROUP=webapps                                     # the group to run as
NUM_WORKERS=4                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=acupuntura.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=acupuntura.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source ../virtual/bin/activate

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../virtual/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-

