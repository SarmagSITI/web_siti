# Langkah Instalasi Project di Komputer
pre requirements:
* python3
* database: mysql

## Buat Virtual Environment
Buat environment dengan nama "sitienv" bisa juga dengan nama lain.

`python3 -m venv sitienv`

atau dengan

`virtualenv -p python3 sitienv`

## Setup Database
Buat Database ikuti langkah [tutorial database](http://www.digitalocean.com/community/tutorials/how-to-use-mysql-or-mariadb-with-your-django-application-on-ubuntu-14-04)

## Setup Virtual environment

Edit file `sitienv/bin/activate`, tambahkan setelah `export VIRTUAL_ENV`:

`export DATABASE_NAME='<your mysql database>'`

`export DATABASE_USER='<your mysql user>'`

`export DATABASE_PASSWORD='<your mysql user password>'`

tambahkan setelah `unset VIRTUAL_ENV`:

`unset DATABASE_NAME`

`unset DATABASE_USER`

`unset DATABASE_PASSWORD`


## Aktifkan Virtual Environment

`source sitienv/bin/activate`


## Clone
CLONE DI LUAR FOLDER ENVIRONMENT !!! JANGAN SATUKAN FOLDER PROJECT DAN ENVIRONTMENT
Clone project dengan syntax berikut,

`git clone https://github.com/SarmagSITI/web_siti.git `

## Install Requierement
Masuk ke folder project `cd web_siti`, lalu install requirement `pip install -r requirements.txt`

## Migrate dan Runserver
migrate: `python manage.py migrate`

runserver: `python manage.py runserver`

Lalu buka 127.0.0.1:8000 pada browser

## Beberapa wiki yang perlu dibaca:
- Development Guide [link](https://github.com/SarmagSITI/web_siti/wiki/Development-Guide)
- Fitur yang ingin dikembangkan [link](https://github.com/SarmagSITI/web_siti/wiki/Fitur)
