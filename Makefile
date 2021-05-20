build:
	(cd ./pythoncalctest && python3 -m pip install -r requirements.txt)
run-main:
	python3 ./pythoncalctest/main.py

coverage:
	rm -rf ./pythoncalctest/build
	(cd ./pythoncalctest && python3 -m pytest --cov=./src --cov-report term-missing --cov-report html:build/reports)
