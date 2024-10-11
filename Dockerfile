FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y build-essential && \
    apt-get install -y python3-dev

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
