FROM python:3.6-slim

WORKDIR /usr/src/app

RUN pip install --no-cache-dir feedparser feedsearch

COPY script.py .

CMD [ "python", "./script.py" ]
