.PHONY: install lint format test coverage run

install:
	conda env create -f environment.yml

lint:
	flake8 models api utils tests scripts

format:
	black models api utils tests scripts

test:
	pytest tests

coverage:
	coverage run -m pytest tests
	coverage report -m

run:
	uvicorn api.api:app --reload
