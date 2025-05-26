from loguru import logger
import os

# Garantir que o diretório de logs exista
os.makedirs("logs", exist_ok=True)

# Configuração do log estruturado
logger.add(
    "logs/algoritimos_api.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
)
