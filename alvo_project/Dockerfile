FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y libpq-dev gcc

RUN apt-get update && apt-get install -y \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*
    
# Definir o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

# Copiar o arquivo de requisitos para o contêiner
COPY req.txt /usr/src/app/

# Instalar as dependências do arquivo de requisitos
RUN pip install --no-cache-dir -r req.txt

# Copiar o restante do código para dentro do contêiner
COPY . /usr/src/app/
