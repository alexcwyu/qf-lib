# QF-Lib

> **Last Updated**: 2026-04-06T16:25:30Z  \
> **Git Hash**: `ba69a25`

Quantitative Finance Library developed at CERN (European Organization for Nuclear Research). A comprehensive Python framework for backtesting trading strategies, portfolio construction, data management, and quantitative analysis.

## Overview

QF-Lib provides a full-stack institutional-grade quantitative finance platform. It features an event-driven backtesting engine, multiple data provider integrations (Bloomberg, Interactive Brokers, Alpaca, Binance, and more), portfolio optimization tools, and extensive analysis and reporting capabilities.

## Key Features

- **Event-Driven Backtesting**: Full simulation engine with broker emulation, order management, position tracking, and strategy orchestration
- **Alpha Models**: Abstract framework for signal generation with exposure management and risk estimation
- **Portfolio Construction**: Mean-variance optimization, Black-Litterman, risk parity, covariance estimation
- **Data Providers**: Bloomberg (BLPAPI, BEAP/HAPI, DL), Interactive Brokers, Alpaca, Binance, Quandl, Yahoo Finance, Portara, Haver, CSV
- **Analysis & Tearsheets**: Backtest overfitting analysis, rolling analysis, exposure analysis, trade analysis, strategy monitoring
- **Custom Containers**: Type-safe QFSeries, QFDataFrame, QFDataArray with financial domain semantics
- **Risk Models**: Covariance estimation (sample, shrinkage, exponential), volatility targeting

## Package Structure

```
src/qf_lib/
    analysis/                   # Post-backtest analysis and tearsheets
        backtests_overfitting/  # Minimum backtest length, overfitting detection
        breakout_strength/      # Trend strength analysis
        exposure_analysis/      # Portfolio exposure analytics
        rolling_analysis/       # Rolling window analysis
        signals_analysis/       # Signal quality evaluation
        strategy_monitoring/    # Live strategy monitoring
        tearsheets/             # Comprehensive strategy reports
        trade_analysis/         # Trade-level P&L analysis
        timeseries_analysis/    # Time series statistical analysis
    backtesting/                # Core backtesting engine
        alpha_model/            # Signal generation framework
        broker/                 # Simulated and live broker interfaces
        contract/               # Contract specifications and mappings
        events/                 # Event system (market data, time, trading)
        execution_handler/      # Order execution simulation
        fast_alpha_model_tester/# Rapid alpha model evaluation
        monitoring/             # Real-time backtest monitoring
        order/                  # Order types and factory
        orders_filter/          # Pre-trade compliance filters
        portfolio/              # Portfolio and position tracking
        position_sizer/         # Position sizing algorithms
        signals/                # Signal objects and management
        strategies/             # Strategy base classes
        trading_session/        # Session orchestration
    brokers/                    # Live broker integrations
    common/                     # Shared types, enums, utilities
        blotter/                # Trade blotter
        enums/                  # Frequency, PriceField, etc.
        risk_parity_boxes/      # Risk parity allocation
        tickers/                # Ticker type hierarchy
        timeseries_analysis/    # Statistical tools
        utils/                  # Date utilities, logging, helpers
    containers/                 # Custom data containers
        dataframe/              # QFDataFrame
        series/                 # QFSeries, various typed series
        futures/                # Futures chain containers
    data_providers/             # Market data access layer
    documents_utils/            # PDF/document generation
    indicators/                 # Technical indicators
    plotting/                   # Chart generation
    portfolio_construction/     # Portfolio optimization
        black_litterman/        # Black-Litterman model
        covariance_estimation/  # Covariance estimators
        optimizers/             # Quadratic and nonlinear optimizers
        portfolio_models/       # Min variance, max diversification, etc.
    settings.py                 # Global configuration
```

## Quick Start

This example uses `PresetDataProvider` with inline synthetic data to demonstrate the data provider and analysis pipeline without any external API keys or data sources.

```python
import numpy as np
import pandas as pd
from datetime import datetime

from qf_lib.common.enums.frequency import Frequency
from qf_lib.common.enums.price_field import PriceField
from qf_lib.common.tickers.tickers import BloombergTicker
from qf_lib.containers.qf_data_array import QFDataArray
from qf_lib.containers.series.qf_series import QFSeries
from qf_lib.data_providers.preset_data_provider import PresetDataProvider

# 1. Generate synthetic OHLCV data
np.random.seed(42)
dates = pd.bdate_range("2020-01-01", "2020-12-31")
ticker = BloombergTicker("EXAMPLE Equity")
n = len(dates)
close = 100 + np.cumsum(np.random.randn(n) * 0.5)
open_ = close + np.random.randn(n) * 0.2
high = np.maximum(open_, close) + np.abs(np.random.randn(n) * 0.3)
low = np.minimum(open_, close) - np.abs(np.random.randn(n) * 0.3)
volume = np.random.randint(1000, 10000, size=n).astype(float)

fields = [PriceField.Open, PriceField.High, PriceField.Low, PriceField.Close, PriceField.Volume]
data = np.stack([open_, high, low, close, volume], axis=-1).reshape(n, 1, 5)
data_array = QFDataArray.create(dates, [ticker], fields, data)

# 2. Create a PresetDataProvider (no external connections needed)
start, end = datetime(2020, 1, 1), datetime(2020, 12, 31)
provider = PresetDataProvider(data_array, start, end, Frequency.DAILY)

# 3. Query price history
prices = provider.get_price(ticker, PriceField.Close, start, end, Frequency.DAILY)
returns = prices.pct_change().dropna()

# 4. Compute basic analytics
series = QFSeries(returns.values, index=returns.index)
print(f"Period: {start.date()} to {end.date()}")
print(f"Total return: {((1 + returns).prod() - 1) * 100:.2f}%")
print(f"Annualized volatility: {returns.std() * np.sqrt(252) * 100:.2f}%")
print(f"Sharpe ratio: {returns.mean() / returns.std() * np.sqrt(252):.3f}")
print(f"Max drawdown: {(prices / prices.cummax() - 1).min() * 100:.2f}%")
```

## Dependencies

- numpy, pandas, scipy
- scikit-learn
- matplotlib
- cvxopt (portfolio optimization)
- Optional: blpapi (Bloomberg), ibapi (Interactive Brokers)

## Documentation

- [Architecture](architecture.md) — System design and components
- [Workflow](workflow.md) — Event flows and processing pipelines
- [State Management](state-management.md) — State lifecycle and data models
- [Development](development.md) — Development guide and best practices

## License

Apache License 2.0 (CERN)
