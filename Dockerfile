# Official Playwright image (includes all deps and browsers)
FROM mcr.microsoft.com/playwright/python:v1.53.0-jammy
WORKDIR /app
# Allure CLI
RUN apt-get update && apt-get install -y wget \
    && wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz \
    && tar -zxvf allure-2.27.0.tgz \
    && mv allure-2.27.0 /opt/allure \
    && ln -s /opt/allure/bin/allure /usr/bin/allure \
    && rm allure-2.27.0.tgz
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["pytest", "--headed", "--alluredir=allure-results"]
