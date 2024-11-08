# Aguas News Scraper

Este proyecto es una herramienta automatizada para obtener noticias relacionadas con el "Consejo Insular de Aguas de Gran Canaria" de Google News. El script se ejecuta de forma periódica para obtener noticias relevantes, almacenarlas en un archivo Excel y enviarlas por correo electrónico.

## Requisitos

- **Python 3.6**: El script de Python requiere Python 3.6.
- **Docker**: Se usa Docker para ejecutar el script en un contenedor.

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu servidor o máquina local:

```bash
git clone https://github.com/tu-usuario/aguas-news.git
cd aguas-news-scraper
```

### 2. Crear el archivo `.env`

Crea un archivo `.env` en el directorio raíz del proyecto con las siguientes variables de entorno:

```plaintext
SMTP_SERVER=server.dir
EMAIL=email@email.com
EMAIL_PASSWORD=XxXxX
NEWS_SEARCH=https://news.google.com/rss/search?q=consejo-insular-de-aguas-de-gran-canaria&hl=es&gl=ES&ceid=ES:es
```

**Importante:** Asegúrate de que el archivo `.env` no se suba a un repositorio público, ya que contiene credenciales sensibles.

### 3. Construir la imagen Docker

Construye la imagen Docker usando el siguiente comando:

```bash
docker build -t aguas-news .
```

### 4. Ejecutar el contenedor manualmente

Para ejecutar el contenedor de forma manual y obtener las noticias, usa el siguiente comando:

```
docker run --rm --env-file .env -v "$(pwd)/output":/usr/src/app/output aguas-news
```

Esto ejecutará el script que obtiene las noticias, las procesa y las guarda en un archivo Excel en el directorio `output`.

## Automatización

Este proyecto está diseñado para ejecutarse automáticamente cada semana. Puedes automatizar la ejecución del script usando un  **cron job** . Para hacerlo, sigue estos pasos:

1. ##### Marcar `run.sh` como ejecutable

   El archivo `run.sh` es un script de shell que facilita la ejecución del contenedor Docker y la construcción de la imagen si es necesario. Asegúrate de que este script sea ejecutable


   ```bash
   chmod +x run.sh
   ```
2. ##### Programar la ejecución semanal con cron

   Abre el crontab para programar la ejecución semanal del script:


   ```
   crontab -e

   ```
   Añade la siguiente línea para que el script se ejecute todos los lunes a las 8:00 AM:

   ```
   0 8 * * 1 /ruta/al/proyecto/run.sh >> /ruta/al/log/output.log 2>&1

   ```
   Esto ejecutará el script semanalmente y almacenará los registros de la ejecución en un archivo `output.log`.
