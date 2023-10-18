### Poketasks


## **Estructura del Proyecto**

El proyecto está organizado usando varios approaches de clean architecture. Debido a la simplicidad del proyecto, el foco
se hizo en la divisón de data logic (repositirios) y service oriented architecture (los servicios para acceder a los repos).


```
├── abilitymanager 
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── templates
│   │   └── abilitymanager
│   ├── tests
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── api
│   ├── __init__.py
│   ├── core
│   │   ├── __init__py
│   │   ├── __pycache__
│   │   ├── api.py
│   │   ├── serializers.py
│   │   ├── tests
│   │   └── urls.py
│   ├── schema.yml
│   └── urls.py
├── core
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── repositories.py
│   ├── services.py
│   ├── signals.py
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       └── test_services.py
├── db.sqlite3
├── dump.rdb
├── manage.py
├── poketasks
│   ├── __init__.py
│   ├── asgi.py
│   ├── celery.py
│   ├── settings.py
│   ├── tasks.py
│   ├── templates
│   │   ├── base.html
│   │   └── swagger-ui.html
│   ├── urls.py
│   └── wsgi.py
├── readme.md
└── requirements.txt

```

* `abilitymanager`: Aplicación relacionada con las vistas para gestionar las habilidades de Pokemones.
* `api`: Aplicación de la API que incluye vistas y serializadores del test.
* `core`: Aplicación principal que incluye el modelo de datos y servicios para Pokemones y Habilidades.


## **Cómo Correr el Proyecto**

Sigue estos pasos para configurar y ejecutar el proyecto:


### **Configuración Inicial**


1. Clona el repositorio desde GitHub:
2. Crea y activa un entorno virtual (se recomienda el uso de `virtualenv` o `venv`):
3. Instala las dependencias desde el archivo `requirements.txt`:


### **Migraciones y Creación de la Base de Datos**



1. Realiza las migraciones:

```
python manage.py migrate

```

5. Crea un superusuario (administrador):


```
python manage.py createsuperuser

```

### **Iniciar el Servidor de Desarrollo de Django**



1. Inicia el servidor de desarrollo de Django:


```
python manage.py runserver

```



4. El servidor se ejecutará en `http://localhost:8000/`.


### **Iniciar Celery y Redis**



1. Inicia un servidor Redis (asegúrate de que Redis esté instalado):


```
redis-server

```

5. Inicia Celery para manejar tareas en segundo plano:


```
celery -A poketasks worker -l info

```



### **Iniciar Celery Beat**



1. Inicia Celery Beat para la planificación de tareas periódicas:


```
celery -A poketasks beat -l info

```



## **Documentación**



* Swagger info:
    * URL: `http://localhost:8000/api/docs/`
    * Métodos HTTP: GET (para buscar) y POST (para crear)
    * Autenticación: Autenticación básica
* Esquema: api/schema.yml 

