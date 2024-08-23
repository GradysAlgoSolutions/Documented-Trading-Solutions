"""Strategy Backtester

# v15: improved implementation

TODO: Replace stub with actual implementation.
"""
import numpy as np
import pandas as pd
from typing import Optional, Dict, Any, List


class Backtester:
    """
    Strategy Backtester.

    Parameters
    ----------
    (see __init__ for parameters)
    """

    def __init__(self, initial_capital: float = 100_000, commission: float = 0.001):
        """Initialise strategy backtester."""
        # TODO: Implement initialisation
        pass

    def fit(self, data: pd.DataFrame, **kwargs) -> "Backtester":
        """
        Fit / train on historical data.

        Parameters
        ----------
        data : pd.DataFrame
            Input data (OHLCV or feature matrix)

        Returns
        -------
        self
        """
        # TODO: Implement training logic
        raise NotImplementedError("fit() not yet implemented")

    def predict(self, data: pd.DataFrame) -> pd.Series:
        """
        Generate predictions / signals.

        Parameters
        ----------
        data : pd.DataFrame
            Input data

        Returns
        -------
        pd.Series
            Predicted values or trading signals
        """
        # TODO: Implement prediction logic
        raise NotImplementedError("predict() not yet implemented")

    def evaluate(self, data: pd.DataFrame, labels: pd.Series) -> Dict[str, float]:
        """
        Evaluate performance on labelled data.

        Returns dict of metric_name -> value.
        """
        # TODO: Implement evaluation metrics
        raise NotImplementedError("evaluate() not yet implemented")
