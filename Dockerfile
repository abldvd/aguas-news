FROM python:3.6-slim

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY script.py .

CMD [ "python", "./script.py" ]
