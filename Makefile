test:
	pytest tests/ -v

lint:
	flake8 . --max-line-length=100

format:
	black . --line-length 100

backtest:
	python main.py --mode backtest

install:
	pip install -r requirements.txt

.PHONY: test lint format backtest install
