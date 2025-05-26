# Algoritimos e API - README

## Índice

1. Descrição do Projeto
2. Gerenciamento de Ambiente com Conda
3. Execução dos Scripts
4. Testes Unitários
5. Sistema de Logs
6. Documentação e Diagramas
7. Execução da API com Docker Compose, Prometheus e Grafana
8. Automatização com Makefile

---

## Descrição do Projeto

Este projeto contém:

* **Algoritmos implementados** na pasta `models`:
  * `computed_property.py`: Decorator para propriedade computada com cache automático.
  * `last_lines_reader.py`: Leitor reverso das últimas linhas de arquivos.
  * `reconcile_accounts_service.py`: Conciliação de transações com tolerância de até ±1 dia.
* **Scripts de execução** na pasta `scripts`:
  * `run_computed_property.py`
  * `run_last_lines_reader.py`
  * `run_reconcile_accounts.py`
* **Dados de exemplo**: pasta `data/`.
* **Gerenciamento de ambiente**: `conda` via `environment.yml`.
* **Testes unitários**: pasta `tests/`.
* **Diagramas e documentação**: pasta `docs/`.
* **Sistema de logs**: estruturado com `loguru`.
* **API**: exposta com `FastAPI` e monitorada via `Prometheus` e `Grafana`.

### URLs importantes:

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000/)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090/)
* Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000/)

---

## Gerenciamento de Ambiente com Conda

1. **Criar o ambiente:**

```bash
conda env create -f environment.yml
```

2. **Ativar o ambiente:**

```bash
conda activate algoritimos_api_env
```

---

## Execução dos Scripts

Dentro do ambiente `algoritimos_api_env`, execute os seguintes comandos:

```bash
python scripts/run_computed_property.py
```

```bash
python scripts/run_last_lines_reader.py
```

```bash
python scripts/run_reconcile_accounts.py
```

---

## Testes Unitários

Execute todos os testes com:

```bash
pytest tests/
coverage run -m pytest
coverage report -m
```

---

## Sistema de Logs

O sistema de logs utiliza `loguru`, com logs estruturados em todos os scripts e na API.
A configuração padrão imprime no console, mas pode ser facilmente ajustada para arquivos ou sistemas externos.

---

## Documentação e Diagramas

Os diagramas dos algoritmos e documentações complementares estão na pasta:

```
docs/
```

Inclui:

* Diagramas Mermaid dos fluxos de cada algoritmo.
* Arquivo Postman para consumir a API.

---

## Execução da API com Docker Compose, Prometheus e Grafana

1. **Subir a API com Prometheus e Grafana:**

```bash
docker compose down --volumes
docker system prune -f
docker compose up --build
```

**Acessar os serviços:**

* API: [http://127.0.0.1:8000](http://127.0.0.1:8000/)
* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* Prometheus: [http://127.0.0.1:9090](http://127.0.0.1:9090/)
* Grafana: [http://127.0.0.1:3000](http://127.0.0.1:3000/)

---

## Automatização com Makefile

Este projeto inclui um **Makefile** para simplificar as tarefas comuns.

### Comandos disponíveis:

* `make env` → cria o ambiente Conda.
* `make install` → instala as dependências.
* `make test` → executa todos os testes.
* `make run` → inicia a API localmente.
* `make docker` → sobe o stack completo com Docker, Prometheus e Grafana.

### Como usar:

```bash
make env
make install
make test
make run
make docker
```
