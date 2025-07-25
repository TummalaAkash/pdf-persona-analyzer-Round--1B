FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app
COPY app/ /app/

RUN apt-get update && apt-get install -y gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    python -c "import nltk; nltk.download('punkt')"

CMD ["python", "main.py"]
