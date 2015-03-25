#!/usr/bin/env bash

set -e

THIS_FILE=$(readlink -f $0)
THIS_DIR=$(dirname ${THIS_FILE})
PROJECT_DIR=$(dirname ${THIS_DIR})
ENVPATH=${VIRTUAL_ENV}
if [ -z ${ENVPATH} ]; then ENVPATH=${PROJECT_DIR}/env; fi
PORT=$1
if [ -z ${PORT} ]; then PORT=8011; fi

source ${PROJECT_DIR}/.server-settings.conf
vex --path ${ENVPATH} python manage.py runserver_plus 0.0.0.0:${PORT}
