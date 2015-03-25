#!/usr/bin/env bash

set -e

# Where is the environment?
ENVPATH=${VIRTUAL_ENV}
if [ -z ${ENVPATH} ]; then ENVPATH=env; fi

# Install missing dependencies
if ! dpkg -s python-pip &> /dev/null; then \
    sudo apt update && sudo apt install -y python-pip; \
fi

# Install vex globally (also installs virtualenv)
type vex &> /dev/null || sudo pip install vex

# Create virtual env folder, if not already in one
if [ -z ${VIRTUAL_ENV} ]; then virtualenv ${ENVPATH}; fi

# Install requirements into virtual env
vex --path ${ENVPATH} pip install -r requirements/dev.txt

echo -e "\nServer settings\n===\n"

# Get server location
read -p "Where is the assets server (http://localhost:8012/)? " server_url
if [ -z ${server_url} ]; then server_url=http://localhost:8012/; fi

# Get auth token
read -p "Auth token for the server? " auth_token
if [ -z ${auth_token} ]; then echo "Auth token required. Exiting"; exit 1; fi

# Store settings to settings file
echo "export WEBSERVICE_URL=${server_url}" > .server-settings.conf
echo "export AUTH_TOKEN=${auth_token}" >> .server-settings.conf
