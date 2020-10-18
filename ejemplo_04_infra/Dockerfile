# Ejemplo de como crear un contenedor docker postgresql
#
# Tomado de: https://docs.docker.com/engine/examples/postgresql_service/
# 
# Crear la imagen con         docker build -t mi_imagen .
# Crear contenedor con        docker run -d --name mi_contenedor -p 5555:5432 mi_imagen
#

# Levantar un servidor ubuntu 16...
FROM ubuntu:16.04

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list

# ...Instalarle postgresql
RUN apt-get update && apt-get install -y python-software-properties software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

USER postgres

# ... indicar que el usuario aministrador "docker" tendrá el password "panasonic"
RUN    /etc/init.d/postgresql start &&\
    psql --command "CREATE USER docker WITH SUPERUSER PASSWORD 'panasonic';" &&\
    createdb -O docker docker

# ... habilitar acceso remoto desde cualquier lugar
RUN echo "host all  all    0.0.0.0/0  md5" >> /etc/postgresql/9.3/main/pg_hba.conf
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

EXPOSE 5432

VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# ... Indicarle el comando para inicializar postgresql
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]