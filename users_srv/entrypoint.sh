#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for database..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "Database started"
fi
#sleep 10
# чистим и мигрируем
python manage.py flush --no-input
python manage.py migrate
# собираем статику
python manage.py collectstatic

exec "$@"