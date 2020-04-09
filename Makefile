default: test

.PHONY: test
test:
	pipenv run python -m pytest tests/

.PHONY: lint
lint:
	pipenv run pylint src/

.PHONY: bandit
bandit:
	pipenv run bandit -r src/