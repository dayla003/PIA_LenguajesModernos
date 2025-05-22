#!/bin/sh

echo "Waiting for MySQL to be ready..."

# Espera hasta que el puerto 3306 de MySQL esté disponible
while ! nc -z db 3306; do
  sleep 1
done

echo "MySQL is up - launching Django..."
exec "$@"
