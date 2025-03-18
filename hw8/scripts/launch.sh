#!/usr/bin/env bash

# Set defaults if not provided in environment
: "${MODULE_NAME:=main}"
: "${VARIABLE_NAME:=app}"
: "${APP_MODULE:=$MODULE_NAME:$VARIABLE_NAME}"
: "${HOST:=0.0.0.0}"
: "${PORT:=8000}"
: "${LOG_LEVEL:=info}"
: "${LOG_CONFIG:=./deploy/configs/logging_uvicorn.ini}"

# Start uvicorn with error handling
echo "Starting uvicorn..."
uvicorn \
    --proxy-headers \
    --host "$HOST" \
    --port "$PORT" \
    "$APP_MODULE"

if [ $? -ne 0 ]; then
    echo "Error starting uvicorn!"
    exit 1
fi

echo "uvicorn started."