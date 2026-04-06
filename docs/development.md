# QF-Lib Development Guide

## Project Setup

```bash
cd qf-lib
pip install -e .
# or with all extras
pip install -e ".[all]"
# or with specific extras
pip install -e ".[detailed_analysis]"  # cvxopt for optimization
```

## Dependencies

**Core**: numpy, pandas, scipy, scikit-learn, matplotlib
**Portfolio optimization**: cvxopt (via `[detailed_analysis]` extra)
**Data providers** (optional):
- `blpapi` - Bloomberg Terminal
- `ibapi` - Interactive Brokers
- `alpaca-py` - Alpaca Markets
- `python-binance` - Binance
- `quandl` - Quandl/Nasdaq Data Link
- `yfinance` - Yahoo Finance

## Project Structure

```
qf-lib/
    src/qf_lib/             # Main package
        analysis/            # Post-backtest analysis
        backtesting/         # Core backtesting engine
        brokers/             # Live broker integrations
        common/              # Shared types and utilities
        containers/          # Custom data containers
        data_providers/      # Market data access
        documents_utils/     # Report generation
        indicators/          # Technical indicators
        plotting/            # Visualization
        portfolio_construction/  # Optimization
        settings.py          # Configuration class
        _version.py          # Version info
    tests/                   # Test suite
```

## Testing

```bash
# Run all tests
pytest tests/

# Run specific test module
pytest tests/test_specific.py

# With coverage
pytest --cov=qf_lib tests/
```

## Code Conventions

### Architecture Patterns

- **Abstract Base Classes**: All major components have abstract base classes (e.g., `DataProvider`, `AlphaModel`, `TradingSession`)
- **Builder Pattern**: Complex objects like `BacktestTradingSession` are constructed via builders
- **Observer Pattern**: The event system uses notifiers (publisher-subscriber)
- **Dependency Injection**: Components receive dependencies via constructor

### Naming

- Classes: `PascalCase` (e.g., `BacktestTradingSession`, `AlphaModel`)
- Methods: `snake_case` (e.g., `get_history`, `calculate_exposure`)
- Enums: `PascalCase` values (e.g., `Frequency.DAILY`, `Exposure.LONG`)
- Private: Leading underscore (e.g., `_calculate_pnl`)
- Type aliases: `PascalCase` (e.g., `QFSeries`, `QFDataFrame`)

### Docstrings

NumPy-style docstrings:

```python
def method(self, param1, param2):
    """
    Brief description.

    Parameters
    ----------
    param1 : type
        Description of param1
    param2 : type
        Description of param2

    Returns
    -------
    return_type
        Description of return value
    """
```

### License Header

All source files include the CERN Apache 2.0 license header.

## Adding a New Data Provider

1. Create a new directory under `data_providers/`
2. Implement a class extending `AbstractPriceDataProvider`:

```python
from qf_lib.data_providers.abstract_price_data_provider import AbstractPriceDataProvider

class MyDataProvider(AbstractPriceDataProvider):
    def get_history(self, tickers, fields, start_date, end_date=None,
                    frequency=None, look_ahead_bias=False, **kwargs):
        # Fetch data from your source
        # Return QFSeries, QFDataFrame, or QFDataArray
        pass

    @property
    def supported_ticker_types(self):
        return {MyTicker}

    @property
    def frequency(self):
        return self._frequency
```

3. Create a corresponding ticker type in `common/tickers/`
4. Add tests

## Adding a New Alpha Model

1. Subclass `AlphaModel`:

```python
from qf_lib.backtesting.alpha_model.alpha_model import AlphaModel
from qf_lib.backtesting.alpha_model.exposure_enum import Exposure

class MyAlphaModel(AlphaModel):
    def __init__(self, data_provider, **params):
        super().__init__(
            risk_estimation_factor=1.0,
            data_provider=data_provider
        )
        # Store strategy parameters

    def calculate_exposure(self, ticker, current_exposure, current_time, frequency):
        # Implement signal logic
        # Return Exposure.LONG, Exposure.SHORT, or Exposure.OUT
        pass
```

2. The base class handles:
   - `get_signal()` orchestration
   - `calculate_fraction_at_risk()` using ATR-based risk estimation
   - Signal object creation with metadata

## Adding a New Analysis Module

1. Create module under `analysis/`
2. Follow the document-based pattern:

```python
from qf_lib.analysis.common.abstract_document import AbstractDocument

class MyAnalysisSheet(AbstractDocument):
    def __init__(self, settings, pdf_exporter, strategy_series, **kwargs):
        super().__init__(settings, pdf_exporter)
        self.strategy_series = strategy_series

    def build_document(self):
        # Add elements to the document
        self._add_header("My Analysis")
        self._add_chart(self._create_returns_chart())
        self._add_table(self._create_stats_table())
```

## Adding a Portfolio Model

1. Implement under `portfolio_construction/portfolio_models/`:

```python
class MyPortfolioModel:
    def get_weights(self, covariance_matrix, expected_returns=None, **kwargs):
        # Use QuadraticOptimizer or NonlinearFunctionOptimizer
        optimizer = QuadraticOptimizer()
        weights = optimizer.get_optimal_weights(P=cov, q=q)
        return weights
```

## Custom Container Types

When returning financial data, use QF-Lib's typed containers:

```python
from qf_lib.containers.series.qf_series import QFSeries
from qf_lib.containers.dataframe.qf_dataframe import QFDataFrame

# These provide domain-specific validation and methods
series = QFSeries(data, index=dates, name="returns")
```

## Settings Configuration

Create a `Settings` object for your environment:

```python
from qf_lib.settings import Settings

settings = Settings(
    output_directory="./output",
    data_directory="./data"
)
```

Additional configuration (database connections, API keys) can be set via environment variables or configuration files.

## Performance Tips

- Use `PrefetchingDataProvider` to batch data requests and avoid redundant API calls
- Set appropriate `look_ahead_bias=False` for backtests (default)
- Use `FastAlphaModelTester` for quick signal evaluation before full backtests
- The `QuadraticOptimizer` uses cvxopt with tight tolerances (`abstol=1e-15`); loosen for faster optimization if appropriate

## Configuration Reference

### Settings (`qf_lib.settings.Settings`)

Settings are loaded from a JSON file (`settings_path`) with optional secret overlay (`secret_path` or `QUANTFIN_SECRET` env var). Keys become nested attributes on the `Settings` object.

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `settings_path` | str | `None` | Path to the public settings JSON file |
| `secret_path` | str | `None` | Path to the secret settings JSON file (merged over public) |
| `QUANTFIN_SECRET` (env) | str | _(not set)_ | JSON string with secret settings (alternative to `secret_path`) |

Common settings JSON keys:

| Key | Type | Description |
|-----|------|-------------|
| `output_directory` | str | Directory for backtest output files (reports, charts, Excel) |
| `data_directory` | str | Directory for cached market data |
| `bloomberg` | dict | Bloomberg connection settings (`host`, `port`) |
| `interactive_brokers` | dict | IB connection settings (`host`, `port`, `client_id`) |
| `alpaca` | dict | Alpaca API settings (`api_key`, `secret_key`, `base_url`) |
| `binance` | dict | Binance API settings (`api_key`, `api_secret`) |

### `BacktestTradingSessionBuilder`

| Method | Parameter | Type | Default | Description |
|--------|-----------|------|---------|-------------|
| `set_backtest_name` | `name` | str | `"Backtest Results"` | Name for the backtest run |
| `set_initial_cash` | `cash` | int | `10000000` | Starting portfolio cash |
| `set_frequency` | `frequency` | `Frequency` | _(required)_ | Trading frequency (`DAILY`, `MIN_1`, `MIN_5`, etc.) |
| `set_commission_model` | `model_type`, `**kwargs` | type, dict | `FixedCommissionModel(0.0)` | Commission model class and parameters |
| `set_slippage_model` | `model_type`, `**kwargs` | type, dict | `PriceBasedSlippage(0.0)` | Slippage model class and parameters |
| `set_position_sizer` | `sizer_type`, `**kwargs` | type, dict | `SimplePositionSizer` | Position sizing algorithm |
| `set_monitor_settings` | `settings` | `BacktestMonitorSettings` | `None` | Settings for real-time monitoring |
| `set_benchmark_tms` | `tms` | `QFSeries` | `None` | Benchmark time series for comparison |

### `PresetDataProvider`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `data` | `QFDataArray` | _(required)_ | Pre-loaded data indexed by dates, tickers, and fields |
| `start_date` | datetime | _(required)_ | Start of the cached data period |
| `end_date` | datetime | _(required)_ | End of the cached data period |
| `frequency` | `Frequency` | _(required)_ | Data frequency (`DAILY`, `MIN_1`, `MIN_5`, etc.) |
| `exp_dates` | dict | `None` | Futures expiration dates mapping (`FutureTicker` -> `QFDataFrame`) |
| `timer` | `Timer` | `None` | Optional timer for controlling current time |

### `FixedCommissionModel`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `commission` | float | `0.0` | Fixed commission per trade |

### `PriceBasedSlippage`

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `slippage_rate` | float | `0.0` | Slippage as fraction of price (e.g., `0.001` = 0.1%) |
| `max_volume_share_limit` | float | `None` | Maximum fraction of volume that can be filled |

### Frequency Enum (`qf_lib.common.enums.frequency.Frequency`)

| Value | Description |
|-------|-------------|
| `Frequency.MIN_1` | 1-minute bars |
| `Frequency.MIN_5` | 5-minute bars |
| `Frequency.MIN_10` | 10-minute bars |
| `Frequency.MIN_15` | 15-minute bars |
| `Frequency.MIN_30` | 30-minute bars |
| `Frequency.MIN_60` | 60-minute (hourly) bars |
| `Frequency.DAILY` | Daily bars |
| `Frequency.WEEKLY` | Weekly bars |
| `Frequency.MONTHLY` | Monthly bars |
| `Frequency.QUARTERLY` | Quarterly bars |
| `Frequency.SEMI_ANNUALLY` | Semi-annual bars |
| `Frequency.YEARLY` | Yearly bars |

## Troubleshooting

### 1. `ValueError: Tickers: [...] are not available in the Data Bundle`
**Cause**: Requested tickers are not present in the `PresetDataProvider`'s data array.
**Solution**: Verify that the tickers passed to `get_price()` / `get_history()` match exactly (including type) the tickers used to construct the `QFDataArray`. Use `BloombergTicker("...")` or the appropriate ticker class.

### 2. `ValueError: Requested start date ... is before data bundle start date`
**Cause**: The backtest or query requests data outside the date range of the `PresetDataProvider`.
**Solution**: Ensure `start_date` and `end_date` in the provider cover the full backtest range plus any warmup periods.

### 3. `AssertionError: The passed data frequency should be at most equal to the frequency of the initially loaded data`
**Cause**: Requesting higher-frequency data than what was loaded (e.g., requesting minute data from a daily provider).
**Solution**: Load data at the highest frequency needed. Downsampling (daily from minute) is supported, but upsampling is not.

### 4. `ImportError: No module named 'blpapi'` / `'ibapi'`
**Cause**: Bloomberg or Interactive Brokers SDK is not installed.
**Solution**: These are optional dependencies. Install with `pip install blpapi` (requires Bloomberg C SDK) or `pip install ibapi`. Use `PresetDataProvider` or `CsvDataProvider` if you do not have access to these services.

### 5. `cvxopt` optimization fails with `ArithmeticError`
**Cause**: The covariance matrix is singular or near-singular, causing the quadratic optimizer to fail.
**Solution**: Use a shrinkage covariance estimator (e.g., `ShrinkageEstimator`) instead of the sample covariance. Check for assets with zero variance or perfect correlation.

### 6. `KeyError: PriceField.Close` when building QFDataArray
**Cause**: The fields dimension of the data array does not contain the requested `PriceField`.
**Solution**: Ensure all required fields (`Open`, `High`, `Low`, `Close`, `Volume`) are included when constructing the `QFDataArray`.

### 7. `TypeError: __init__() missing required positional argument: 'pdf_exporter'`
**Cause**: `BacktestTradingSessionBuilder` requires a `Settings`, `PDFExporter`, and `ExcelExporter`.
**Solution**: All three are mandatory constructor arguments. For testing without PDF output, create minimal instances: `PDFExporter(settings)` and `ExcelExporter(settings)`.

### 8. Backtest produces flat equity curve (no trades)
**Cause**: Alpha model always returns `Exposure.OUT`, or the position sizer blocks all orders.
**Solution**: Debug the `calculate_exposure()` method. Log the exposure values at each step. Check that the data provider returns valid prices for the backtest period.

## Security Considerations

### API Key Management
- Bloomberg, Interactive Brokers, Alpaca, and Binance credentials should be stored in the `secret_settings.json` file or the `QUANTFIN_SECRET` environment variable -- never in the public `settings.json`.
- The `Settings` class merges public and secret configurations, keeping credentials separate from shareable settings.

### Credential Storage
- `secret_settings.json` should be excluded from version control (add to `.gitignore`).
- The `QUANTFIN_SECRET` environment variable accepts a JSON string, suitable for CI/CD pipelines and container deployments where files are less convenient.
- Database connection strings for data caching should use the secret settings path.
- Avoid logging `Settings` objects directly, as they may contain credentials as attributes.

### Network Security
- Bloomberg (`blpapi`) connections use the Bloomberg Terminal's own security. Ensure the terminal is properly authenticated.
- Interactive Brokers connections use the TWS/Gateway API on localhost. Do not expose the TWS API port (default 7497/7496) to the network.
- Alpaca and Binance providers communicate over HTTPS. Verify that `base_url` settings use `https://` prefixes.
- `PresetDataProvider` and `CsvDataProvider` are entirely local and make no network calls.

### Safe Practices
- Use `look_ahead_bias=False` (the default) in all data provider calls during backtesting to prevent future data from leaking into past decisions.
- Set `max_volume_share_limit` in the slippage model to prevent unrealistic fills in backtests.
- When generating PDF reports (`PDFExporter`), ensure the `output_directory` has appropriate filesystem permissions. Reports may contain proprietary strategy details.
- In production, run the backtesting framework under a service account with minimal filesystem and network permissions.
- Regularly audit data provider configurations to ensure no unintended data sources are active.

---
## See Also
- [README](README.md) — Project overview and quick start
- [Architecture](architecture.md) — System design and components
- [Workflow](workflow.md) — Event flows and processing pipelines
- [State Management](state-management.md) — State lifecycle and data models
