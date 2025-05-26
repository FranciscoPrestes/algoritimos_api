import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import FastAPI
from api.computed_router import router, Example

@pytest.fixture(scope="function")
def app() -> FastAPI:
    """
    Fixture para criar uma instância da aplicação FastAPI
    com o router de Computed Property incluído.
    """
    app = FastAPI()
    app.include_router(router, prefix="/computed")
    return app

@pytest.mark.asyncio
async def test_get_computed_property(app: FastAPI) -> None:
    """
    Testa o endpoint GET /computed/example/{value}
    verificando se o valor computado está correto.
    """
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        value = 10.0
        response = await client.get(f"/computed/example/{value}")
        assert response.status_code == 200
        data = response.json()
        assert data["value"] == value
        assert data["double"] == value * 2

def test_example_computed_property() -> None:
    """
    Testa diretamente a classe Example e a ComputedProperty.
    """
    value = 5.0
    example = Example(value)

    # Primeiro cálculo - deve computar
    double_first = example.double
    assert double_first == 10.0

    # Segundo cálculo - deve usar cache
    double_second = example.double
    assert double_second == 10.0

    # Alteração no valor - deve invalidar o cache
    example.value = 7.0
    double_new = example.double
    assert double_new == 14.0
