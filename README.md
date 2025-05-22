# Tarot Egipcio Gold

Sistema web para la lectura de tarot egipcio. Esta aplicación proporciona una experiencia interactiva para la interpretación de cartas del tarot egipcio.

## Características

- API REST para consulta de cartas egipcias
- Sistema de generación aleatoria de cartas
- Base de datos SQLite para almacenamiento de cartas
- Interfaz web para lectura de tarot

## Requisitos

- Python 3.x
- Django
- Django REST Framework
- SQLite

## Instalación

1. Clonar el repositorio
2. Crear un entorno virtual:
   ```bash
   python -m venv virtual
   source virtual/bin/activate  # En Windows: virtual\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install django djangorestframework
   ```
4. Configurar la base de datos:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Ejecución

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

O usar el script de inicio:
```bash
start_server.bat
```

## Estructura del Proyecto

- `app_tarot_egipcio/`: Contiene la lógica principal de la aplicación
- `static/`: Archivos estáticos (CSS, JavaScript, imágenes)
- `cartas_egipcias.json`: Base de datos de las cartas
- `db.sqlite3`: Base de datos SQLite

## API Endpoints

- `GET /api/cartas/`: Lista todas las cartas
- `GET /api/cartas/random/`: Obtiene una carta aleatoria

## Contribución

Las contribuciones son bienvenidas. Por favor, crea un issue o pull request para sugerir mejoras o reportar problemas.

## Licencia

[MIT License](LICENSE)
