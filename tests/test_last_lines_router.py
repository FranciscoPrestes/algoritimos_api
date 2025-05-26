import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import FastAPI
from api.last_lines_router import router

@pytest.fixture(scope="function")
def app() -> FastAPI:
    """
    Fixture para criar uma instância da aplicação FastAPI
    com o router de Last Lines incluído.
    """
    app = FastAPI()
    app.include_router(router, prefix="/last-lines")
    return app

@pytest.mark.asyncio
async def test_read_last_lines(app: FastAPI) -> None:
    """
    Testa o endpoint POST /last-lines/
    verificando se retorna corretamente as últimas linhas solicitadas.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {
            "content": "linha1\nlinha2\nlinha3\nlinha4\nlinha5",
            "num_lines": 3
        }
        response = await client.post("/last-lines/", json=payload)
        assert response.status_code == 200

        data = response.json()
        assert data["lines"] == ["linha3", "linha4", "linha5"]
