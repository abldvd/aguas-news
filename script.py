import os
import feedparser
from time import mktime
import pandas as pd
from datetime import datetime, timedelta

import smtplib
from email.mime.text import MIMEText

news_feed = feedparser.parse(os.getenv("NEWS_SEARCH"))
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


## Enviar correo informativo
# Recuperamos variables de entorno
smtp_server = os.getenv("SMTP_SERVER")
email = os.getenv("EMAIL")
email_password = os.getenv("EMAIL_PASSWORD")


# Construir el contenido HTML del correo
html_content = "<html><body>"
html_content += "<h2>Noticias Recientes</h2>"
html_content += "<ul>"

# Agregar cada entrada del DataFrame como un elemento de lista con un enlace
for _, row in df_new_entries.iterrows():
    titulo, sitio = row['title'].split(" - ", 1)
    html_content += f"<li><strong>{row['published']}</strong> - {titulo} - <a href='{row['link']}'>{sitio}</a></li>"

html_content += "</ul>"
html_content += "</body></html>"

message = MIMEText(html_content, "html")
message["Subject"] = "Resumen de noticias semanales"
message["From"] = email
message["To"] = email

# Send the email
with smtplib.SMTP(smtp_server, 25) as server:
    server.login(email, email_password)
    server.sendmail(email, email, message.as_string())

print(f'Correo enviado a {email}')