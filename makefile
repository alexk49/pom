test:
		./.venv/bin/python3 -m doctest -v ./ptimer/ptimer.py
		./.venv/bin/python3 -m unittest discover -v
