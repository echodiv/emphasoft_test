#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for database..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Database started"
fi

exec "$@"