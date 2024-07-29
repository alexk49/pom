test:
		./.venv/bin/python3 -m doctest -v ./pom/pom.py
		./.venv/bin/python3 -m unittest discover -v
