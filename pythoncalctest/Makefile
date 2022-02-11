build:
	python3 -m pip install -r requirements.txt

run-main:
	python3 main.py

coverage:
	rm -rf ./build
	python3 -m pytest -vv --cov-config=.coveragerc --cov=. --cov-report term-missing --cov-report html:build/reports --cov-branch --cov-fail-under=95

lint:
	pylint ./src

mypy:
	mypy ./src

review:	lint mypy coverage
