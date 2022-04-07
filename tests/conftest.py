"""
Pytest configuration and shared fixtures.
"""
import pytest
import pandas as pd
import numpy as np
from tests.fixtures import make_ohlcv


@pytest.fixture(scope="session")
def ohlcv_data():
    return make_ohlcv(252)


@pytest.fixture(scope="session")
def short_ohlcv():
    return make_ohlcv(50)
