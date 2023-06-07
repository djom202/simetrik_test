default: runtest

runtest:
	@python3 -m pytest ./tests

report:
	@python3 -m pytest -sv --html reports/report.html

env:
	@python3 -m venv env

install:
	@pip3 install -r requirements.txt

PHONY: runtest