# Crehana test resolution

The project uses the following technologies:
+ Django 3.1.5
+ Djangorestframework 3.12.2
+ Celery 5.0.5
+ django-celery-results 2.0.0
+ gevent 20.12.1
+ redis 3.5.3

## System requirements

+ [Git](https://git-scm.com/)
+ [Redis](https://github.com/microsoftarchive/redis/releases)
+ [Python 3.8.3](https://www.python.org/downloads/release/python-383/)

# Configure locale

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
mkdir prueba-crehana
cd prueba-crehana
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

### 7. Create super user

```
py manage.py createsuperuser --email admin@example.com --username admin
```

### 8. Load data

```
py manage.py loaddata load_data.json
```

### 8. Start project

```
py manage.py runserver
```

### 9. Start celery. We locate ourselves in the project folder and initialize the virtual environment, then execute the following command

```
celery -A crehana worker -l info -P gevent
```

Visit [http://localhost:8000/admin/](http://localhost:8000/admin/). You should see admin django ;)


## Tests

### 1. Security: Configure postman to perform the query with basic authentication. Put the credentials of the super user

### 2. To perform a test we need to open Post Man and place the following url: http://localhost:8000/create_event/

### 3. Select the POST method and send the following JSON

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
+ [Django 3.1.5](https://www.djangoproject.com/)
+ [Django REST Framework 3.12.2](http://www.django-rest-framework.org/)
+ [Redis](https://redis.io/)

## Authors

* **Brayan Calcina Aguilar**
