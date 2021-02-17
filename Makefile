# what is the purpose of PHONY - https://stackoverflow.com/questions/2145590/what-is-the-purpose-of-phony-in-a-makefile
.PHONY: init

init::
	pip install --upgrade pip setuptools
	pip install -r requirements.txt

test:
	python -m pytest -vvs tests

black:
	black .

black-check:
	black --check .

flake8:
	flake8 --exclude==.venv,node_modules .

lint: black-check flake8
