FROM python:3.10-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN apt-get update && \
    apt-get install -y libgl1 poppler-utils && \
    pip install --no-cache-dir -r requirements.txt

COPY app/ .
COPY data/ /app/data/
COPY images/ /app/images/

CMD ["python", "main.py"]
