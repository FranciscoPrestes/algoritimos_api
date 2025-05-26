from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse
from api.reconcile_router import router as reconcile_router
from api.last_lines_router import router as last_lines_router
from api.computed_router import router as computed_router
from prometheus_fastapi_instrumentator import Instrumentator

app: FastAPI = FastAPI(
    title="Algoritimos API",
    description="API que expõe algoritmos de conciliação, leitura reversa e propriedade computada.",
    version="1.0.0"
)

# Inclusão das rotas isoladas por serviço
app.include_router(reconcile_router, prefix="/reconcile", tags=["Reconcile"])
app.include_router(last_lines_router, prefix="/last-lines", tags=["Last Lines"])
app.include_router(computed_router, prefix="/computed", tags=["Computed Property"])

@app.get("/", include_in_schema=False)
async def root() -> RedirectResponse:
    """
    Redireciona a rota raiz (/) para a página informativa (/about).

    Returns:
        RedirectResponse: Redirecionamento HTTP para /about.
    """
    return RedirectResponse(url="/about")

@app.get("/about", response_class=HTMLResponse)
async def about() -> str:
    """
    Exibe informações sobre a API em formato HTML apresentável.

    Returns:
        str: Conteúdo HTML com instruções e links úteis.
    """
    return """
    <html>
        <head>
            <title>Algoritimos API - Sobre</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                h1 { color: #333; }
                ul { list-style-type: square; }
                a { text-decoration: none; color: #007BFF; }
                a:hover { text-decoration: underline; }
                code { background-color: #f2f2f2; padding: 2px 4px; border-radius: 4px; }
            </style>
        </head>
        <body>
            <h1>🚀 Bem-vindo à Algoritimos API!</h1>
            <p><strong>Documentação:</strong></p>
            <ul>
                <li><a href="/docs" target="_blank">Swagger</a></li>
                <li><a href="/redoc" target="_blank">ReDoc</a></li>
            </ul>

            <p><strong>Monitoramento:</strong></p>
            <ul>
                <li><a href="/metrics" target="_blank">Prometheus</a></li>
                <li><a href="http://localhost:3000" target="_blank">Grafana (rodando com Docker Compose) User: admin pass: admin</a></li>
            </ul>

            <p><strong>Endpoints Principais:</strong></p>
            <ul>
                <li>Conciliação: <code>/reconcile</code></li>
                <li>Leitura Reversa: <code>/last-lines</code></li>
                <li>Propriedade Computada: <code>/computed</code></li>
            </ul>

            <p><strong>Saúde:</strong> <a href="/health" target="_blank">/health</a></p>
        </body>
    </html>
    """

@app.get("/health")
async def health_check() -> dict[str, str]:
    """
    Endpoint de verificação de saúde da API.

    Returns:
        dict: Status da aplicação.
    """
    return {"status": "OK"}

# Exposição das métricas Prometheus
Instrumentator().instrument(app).expose(app)
