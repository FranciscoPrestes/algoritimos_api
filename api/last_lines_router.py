from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class LastLinesInput(BaseModel):
    content: str
    num_lines: int = 10  # número de linhas que deseja retornar

@router.post("/")
def read_last_lines(input_data: LastLinesInput):
    """
    Lê as últimas linhas de uma mensagem de texto enviada como JSON.

    Args:
        input_data (LastLinesInput): Mensagem de texto com conteúdo e quantidade de linhas.

    Returns:
        dict: Últimas linhas do conteúdo.
    """
    content_lines = input_data.content.strip().splitlines()
    last_lines = content_lines[-input_data.num_lines:]
    return {"lines": last_lines}
