# Usar imagem oficial leve do Python
FROM python:3.10-slim

# Evita buffering de logs
ENV PYTHONUNBUFFERED=1

# Instalar dependências básicas do sistema
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Criar diretório de trabalho
WORKDIR /app

# Copiar os arquivos de dependências
COPY requirements.txt .

# Instalar dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do projeto
COPY . .

# Carregar variáveis de ambiente automaticamente (opcional)
# ou usar --env-file no docker run

# Expor a porta da API
EXPOSE 8000

# Comando padrão para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
