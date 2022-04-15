"""
Sample market data fixtures for tests.
"""
import numpy as np
import pandas as pd
import pytest


def make_ohlcv(n: int = 252, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic OHLCV data for testing."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range("2023-01-01", periods=n, freq="B")
    close = 100.0 * np.cumprod(1 + rng.normal(0.0005, 0.015, n))
    high   = close * (1 + rng.uniform(0, 0.02, n))
    low    = close * (1 - rng.uniform(0, 0.02, n))
    open_  = close * (1 + rng.normal(0, 0.005, n))
    volume = rng.integers(1_000_000, 10_000_000, n)
    return pd.DataFrame(
        {"open": open_, "high": high, "low": low,
         "close": close, "volume": volume},
        index=dates,
    )


@pytest.fixture
def sample_ohlcv():
    return make_ohlcv()
