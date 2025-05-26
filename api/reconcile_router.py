from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from models.reconcile_accounts_service import ReconcileAccountsService

router = APIRouter()


class ReconcileInput(BaseModel):
    transactions_1: List[List[str]]
    transactions_2: List[List[str]]


class ReconcileOutput(BaseModel):
    transactions_1: List[List[str]]
    transactions_2: List[List[str]]


@router.post("/", response_model=ReconcileOutput)
async def reconcile(input_data: ReconcileInput) -> ReconcileOutput:
    """
    Executa a conciliação entre duas listas de transações.

    Args:
        input_data (ReconcileInput): Dados contendo duas listas de transações.

    Returns:
        ReconcileOutput: Resultado da conciliação com anotações.
    """
    service = ReconcileAccountsService(
        transactions_1=input_data.transactions_1,
        transactions_2=input_data.transactions_2
    )
    reconciled_1, reconciled_2 = service.reconcile()
    
    return ReconcileOutput(
        transactions_1=reconciled_1,
        transactions_2=reconciled_2
    )
