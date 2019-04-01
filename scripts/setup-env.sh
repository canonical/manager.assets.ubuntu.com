#! /usr/bin/env bash

# Get assets server settings
if [ -t 1 ] && [ -z "${WEBSERVICE_URL:-}" ]; then
    echo "Enter the URL for the assets webservice (e.g. https://assets.staging.ubuntu.com, or http://localhost:8018):"
    read WEBSERVICE_URL
    export WEBSERVICE_URL=${WEBSERVICE_URL}
    echo "WEBSERVICE_URL=${WEBSERVICE_URL}" >> .env.local
fi
if [ -t 1 ] && [ -z "${AUTH_TOKEN:-}" ]; then
    echo "Enter the authentication token for the assets webservice:"
    read AUTH_TOKEN
    export AUTH_TOKEN=${AUTH_TOKEN}
    echo "AUTH_TOKEN=${AUTH_TOKEN}" >> .env.local
fi
