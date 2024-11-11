# Trading Tools Suite v28.84

A comprehensive collection of algorithmic trading tools, ML models, and backtesting utilities.

## Features

- Multiple trading strategies (mean reversion, momentum, pairs trading, arbitrage)
- ML price prediction models (LSTM, XGBoost, Transformer, RL agents)
- Technical indicators library
- Full backtesting engine with performance metrics
- Risk management and portfolio optimization
- Automated data pipeline

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from strategies.momentum import MomentumStrategy
from utils.backtester import Backtester
from utils.data_fetcher import DataFetcher

# Fetch data
fetcher = DataFetcher()
data = fetcher.get_ohlcv("AAPL", period="2y")

# Run strategy
strategy = MomentumStrategy(lookback=20)
bt = Backtester(strategy)
results = bt.run(data)
print(results.summary())
```

## Structure

```
├── strategies/     # Trading strategy implementations
├── models/         # ML prediction models
├── indicators/     # Technical indicators
├── utils/          # Backtesting, risk management, data fetching
├── data/           # Data pipeline and preprocessing
└── tests/          # Unit and integration tests
```

## Status

Work in progress. See individual module docstrings for implementation status.
