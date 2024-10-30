import feedparser
from datetime import datetime, timedelta
from time import mktime
import pandas as pd

news_feed = feedparser.parse("https://news.google.com/rss/search?q=consejo-insular-de-aguas-de-gran-canaria&hl=es&gl=ES&ceid=ES:es")
fecha_desde = datetime.today() - timedelta(days=14)

#Extraer excel existente
excel_file = './output/news.xlsx'
try:
    df_existing = pd.read_excel(excel_file, engine='openpyxl')
except FileNotFoundError:
    # Si el archivo no existe, se crea un nuevo DataFrame
    df_existing = pd.DataFrame(columns=['published', 'title', 'link'])

# Iterar sobre las entradas del feed
data = []
for entry in news_feed.entries:
    fecha_publicacion = datetime.fromtimestamp(mktime(entry.published_parsed))
    if fecha_publicacion > fecha_desde:
        data.append({
            'published': fecha_publicacion.strftime('%d-%m-%Y'),  # Formato de fecha
            'title': entry.title,
            'link': entry.link,
        })
df_new_entries = pd.DataFrame(data)

# Concatenar los datos existentes con los nuevos
df_combined = pd.concat([df_existing, df_new_entries], ignore_index=True)
# Eliminar entradas duplicadas
df_combined = df_combined.drop_duplicates(subset=['title', 'link'], keep='first')

# Exportar el DataFrame combinado a un archivo Excel
df_combined.to_excel(excel_file, index=False, engine='openpyxl')

print(f'Datos añadidos al archivo {excel_file}')