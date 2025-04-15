FROM python:3.12-slim

WORKDIR /app

# Install CA certificates for SSL
RUN apt-get update && apt-get install -y ca-certificates

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]