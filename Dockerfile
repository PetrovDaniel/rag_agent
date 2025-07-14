FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    iputils-ping \
    && rm -rf /var/lib/apt/lists/*

# Копируем файлы
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY app/ .

# Порт
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]