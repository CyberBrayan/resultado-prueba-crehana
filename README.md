# Resolución de prueba crehana

El proyecto utiliza las siguientes tecnologías:
+ Django 3.1.5
+ Djangorestframework 3.12.2
+ Celery 5.0.5
+ django-celery-results 2.0.0
+ gevent 20.12.1
+ redis 3.5.3

## Requerimientos del sistema

+ [Git](https://git-scm.com/)
+ [Redis](https://github.com/microsoftarchive/redis/releases)
+ [Python 3.8.3](https://www.python.org/downloads/release/python-383/)

# Configurar entorno local

## Start REDIS

### 1. Download REDIS .zip

```
https://github.com/microsoftarchive/redis/releases
```

### 2. Locate the zip file in C and extract and execute the file

```
redis-server.exe
```

## Configure Django project

#### 1. Create the project directory

```
mkdir tutorial
cd tutorial
```

### 2. Clone the project in the created directory

```
git clone https://github.com/CyberBrayan/resultado-prueba-crehana/tree/master.git
```

#### 3. Create a virtual environment to isolate our package dependencies locally

```
py -m venv env
```

### 4. Initialize the virtual environment

```
env\Scripts\activate
```

### 5. Install dependencies

```
pip install -r requeriments.txt
```

### 5. Prepare for data migration

```
py manage.py makemigrations
```

### 6. Migrate data

```
py manage.py migrate
```

### 7. We create a super user

```
py manage.py createsuperuser --email admin@example.com --username admin
```

### 8. We upload information

```
py manage.py loaddata load_data.json
```

### 8. We execute the project

```
py manage.py runserver
```

### 9. We initialize celery. We locate ourselves in the project folder and initialize the virtual environment, then execute the following command

```
celery -A crehana worker -l info -P gevent
```

Visit [http://localhost/admin](http://localhost/admin). You should see admin django ;)


## Tests

### 1. To perform a test we need to open Post Man and place the following url: http://localhost:8000/create_event/

### 2. Select the POST method and send the following JSON

```
{
    "event_type": 3,
    "minute": 12,
    "inscription": 4
}
```

## Languages used
+ [Python](https://www.python.org/)


## Tools used
+ [Nginx](https://www.nginx.com/)
+ [Gunicorn](https://gunicorn.org/)
+ [Docker 1.12.1](https://www.docker.com/)
+ [Django 2.1.7](https://www.djangoproject.com/)
+ [PostgreSQL 9.6.0](http://www.postgresql.org/)
+ [Docker compose 1.8.0](https://docs.docker.com/compose/)
+ [Django REST Framework 3.9.1](http://www.django-rest-framework.org/)


## Helpful resources
+ [Django Development with Docker Compose and Machine](https://realpython.com/django-development-with-docker-compose-and-machine/)
+ [Dockerizing Django projects](http://ruddra.com/2016/08/14/docker-django-nginx-postgres/)
+ [Extension of Owais Lane's blog post](http://geezhawk.github.io/using-react-with-django-rest-framework)
+ [YouTube Playlist on Django Rest Framework](https://www.youtube.com/playlist?list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)
+ [JSON Web Tokens With Django REST Framework](https://www.youtube.com/watch?v=Fhcn2qx-4VQ)
+ [Full Stack Python](http://www.fullstackpython.com/)
+ [Write your first Django App](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
+ [Quick Django tutorial](http://drksephy.github.io/2015/07/16/django/)
+ [Django REST framework](http://www.django-rest-framework.org/tutorial/1-serialization/)


## Authors

* **Robert Arzola Castillo** - *Initial work*


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
