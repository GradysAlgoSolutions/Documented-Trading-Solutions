"""
Trading Tools - Main Entry Point (v8)

Run backtests, live trading, or analysis from the command line.
"""

import argparse
import logging
from utils.config_loader import ConfigLoader
from utils.logger import setup_logger

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description="Trading Tools Suite")
    parser.add_argument("--mode", choices=["backtest", "live", "analyze"],
                        default="backtest", help="Run mode")
    parser.add_argument("--strategy", type=str, default="momentum",
                        help="Strategy to run")
    parser.add_argument("--symbol", type=str, default="SPY",
                        help="Trading symbol")
    parser.add_argument("--config", type=str, default="config.yaml",
                        help="Config file path")
    args = parser.parse_args()

    config = ConfigLoader(args.config).load()
    setup_logger(config.get("logging", {}))

    logger.info("Starting trading tools in %s mode", args.mode)

    # TODO: Wire up strategy selection and execution
    raise NotImplementedError(f"Mode {args.mode} not yet implemented")


if __name__ == "__main__":
    main()
