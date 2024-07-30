export PYTHONPATH := $(shell pwd)

test:
		./.venv/bin/python3 -m doctest -v ./pom/timers.py
		./.venv/bin/python3 -m unittest discover -v

.PHONY: test
