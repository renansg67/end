# Dockerfile (Versão Corrigida)

# 1. Imagem Base
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD streamlit run app.py --server.port $PORT --server.enableCORS=false --server.enableXsrfProtection=false