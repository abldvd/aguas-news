FROM python:3.8-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir pygooglenews 

COPY script.py .

CMD [ "python", "./script.py" ]
