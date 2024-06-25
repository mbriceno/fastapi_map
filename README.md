Map My World
============

Microservicio para gestionar Categorías y Ubicaciones del App.

Development Stack:
------------------

- Python 3.11
- FastApi 0.111
- Postgresql 15
- Pytest 8.2

Docker container:
-----------------

Ejecutar el proyecto en Docker:

```sh
# Build
docker compose up -d
```

El Proyecto cuenta con feature test implementados con pytest

Para ejecuatar los test desde el contenedor:

```sh
docker compose run --rm python pytest
```

Como todo proyecto en FastApi puedes consultar la documentación en el navegador:

http://localhost:8000/docs
