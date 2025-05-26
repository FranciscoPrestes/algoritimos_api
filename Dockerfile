FROM continuumio/miniconda3

WORKDIR /app

# Copia arquivos de dependência
COPY environment.yml .

# Cria ambiente Conda
RUN conda env create -f environment.yml

# Ativa ambiente
SHELL ["conda", "run", "-n", "algoritimos_api_env", "/bin/bash", "-c"]

# Instala dependências adicionais se necessário
COPY . .

# Comando default: iniciar API
CMD ["conda", "run", "-n", "algoritimos_api_env", "uvicorn", "api.api:app", "--host", "0.0.0.0", "--port", "8000"]
