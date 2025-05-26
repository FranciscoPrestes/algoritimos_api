import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import FastAPI
from api.reconcile_router import router

@pytest.fixture(scope="function")
def app() -> FastAPI:
    """
    Fixture para criar uma instância da aplicação FastAPI
    com o router de Reconcile incluído.
    """
    app = FastAPI()
    app.include_router(router, prefix="/reconcile")
    return app

@pytest.mark.asyncio
async def test_reconcile(app: FastAPI) -> None:
    """
    Testa o endpoint POST /reconcile/
    verificando se a conciliação retorna os campos esperados.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {
            "transactions_1": [["2024-05-01", "desc1", "100", "BRL"]],
            "transactions_2": [["2024-05-02", "desc1", "100", "BRL"]]
        }
        response = await client.post("/reconcile/", json=payload)
        assert response.status_code == 200

        data = response.json()
        assert "transactions_1" in data
        assert "transactions_2" in data

        # Valida se o status está entre os possíveis
        status = data["transactions_1"][0][-1]
        assert status in {"FOUND", "MISSING", "INVALID"}
