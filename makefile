export PYTHONPATH := $(shell pwd)
VENV_NAME?=venv
VENV_DIR?=./.$(VENV_NAME)
PIP=${VENV_DIR}/bin/pip

all: venv setup test
venv:
		 test -d $(VENV_DIR) || python3 -m venv $(VENV_DIR)
setup: venv
		 $(PIP) install --upgrade pip
		 $(PIP) install black mypy flake8
test: venv setup
		$(VENV_DIR)/bin/python3 -m doctest -v ./pom/timers.py
		$(VENV_DIR)/bin/python3 -m unittest discover -v
clean:
		rm -rf $(VENV_NAME)
		# delete pycache files
		py3clean .

.PHONY: test setup clean venv
