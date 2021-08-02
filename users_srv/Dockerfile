# pull official base image
FROM python:3.8
# set work directory
WORKDIR /usr/src/users_srv
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# for db ping
RUN apt-get update \
    && apt-get install -y netcat

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
# copy project
COPY . .

ENTRYPOINT ["/usr/src/users_srv/entrypoint.sh"]