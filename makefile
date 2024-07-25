test:
		./.venv/bin/python3 -m doctest -v ./pt/pt.py
		./.venv/bin/python3 -m unittest discover -v
