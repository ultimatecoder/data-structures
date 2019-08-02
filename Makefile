install-dev:
	pip install pipenv
	pipenv install --dev
test: unit-test type-check
unit-test:
	pipenv run pytest data_structures
lint: type-check
	pipenv run flake8
type-check:
	pipenv run mypy data_structures
