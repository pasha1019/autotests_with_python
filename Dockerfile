FROM python:3.11-alpine3.18

# Установка всех зависимостей в одном слое с очисткой
RUN apk update && apk add --no-cache \
    chromium \
    chromium-chromedriver \
    tzdata \
    openjdk17-jre-headless \
    curl \
    tar && \
    # Установка Allure (последняя стабильная версия)
    curl -sSL -o allure-2.24.1.tgz \
    https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.24.1/allure-commandline-2.24.1.tgz && \
    tar -zxvf allure-2.24.1.tgz -C /opt/ && \
    ln -sf /opt/allure-2.24.1/bin/allure /usr/bin/allure && \
    # Очистка временных файлов
    rm -rf allure-2.24.1.tgz /var/cache/apk/*

WORKDIR /app

# Копируем и устанавливаем зависимости отдельным слоем для кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY . .

# Устанавливаем переменные окружения
ENV PYTHONPATH=/app \
    ALLURE_RESULTS_DIR=/app/allure-results \
    PATH="/opt/allure-2.24.1/bin:${PATH}"

# Создаем директорию для отчетов
RUN mkdir -p /app/allure-results

CMD ["python", "-m", "pytest", "--alluredir=/app/allure-results"]