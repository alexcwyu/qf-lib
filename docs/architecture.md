# QF-Lib Architecture

## System Architecture Overview

QF-Lib follows an event-driven architecture for backtesting, with clean separation between data provision, signal generation, order management, and execution. The design supports both backtesting and live trading through common interfaces.

```mermaid
graph TB
    subgraph "Data Layer"
        DP[DataProvider] --> |get_history| CACHE[Prefetching Cache]
        BLOOMBERG[Bloomberg] --> DP
        IB[Interactive Brokers] --> DP
        ALPACA[Alpaca] --> DP
        BINANCE[Binance] --> DP
        CSV[CSV Files] --> DP
        YAHOO[Yahoo Finance] --> DP
    end

    subgraph "Backtesting Engine"
        TS[TradingSession] --> EM[EventManager]
        EM --> |dispatch| NOT[Notifiers]
        NOT --> |market_close| STRAT[Strategy]
        STRAT --> AM[AlphaModel]
        AM --> |Signal| PS[PositionSizer]
        PS --> |Order| OF[OrderFactory]
        OF --> |Order| BROKER[Broker]
        BROKER --> |Fill| PORT[Portfolio]
        PORT --> MON[Monitor]
    end

    subgraph "Portfolio Construction"
        COV[Covariance Estimator] --> OPT[Optimizer]
        BL[Black-Litterman] --> OPT
        OPT --> WEIGHTS[Portfolio Weights]
    end

    subgraph "Analysis & Reporting"
        PORT --> TS_ANAL[Tearsheets]
        PORT --> ROLL[Rolling Analysis]
        PORT --> TRADE[Trade Analysis]
        PORT --> EXP[Exposure Analysis]
    end
```

## Trading Paradigm & Key Features

| Feature | Support | Details |
|---------|---------|---------|
| Backtesting Approach | Event-driven | Full event loop with broker emulation, order management, and position tracking |
| Live Trading | Yes | Same TradingSession interface with live data providers and brokers |
| Paper Trading | Yes | Simulated broker with realistic order execution for paper trading |
| Multi-Asset | Yes | Equities, futures, crypto, and more via abstract Ticker/Contract system |
| Data Feeds | Multiple providers | Bloomberg (BLPAPI, BEAP, DL), Interactive Brokers, Alpaca, Binance, Quandl, Yahoo Finance, CSV |
| ML Integration | No | No built-in ML; alpha models are rule-based with exposure signals (LONG/SHORT/OUT) |
| Risk Management | Built-in | Position sizing, stop-loss support, fraction-at-risk estimation, exposure analysis |
| Optimization | No | No built-in hyperparameter optimization; FastAlphaModelTester for rapid signal evaluation |
| Execution | Both | Simulated broker for backtesting; live via Interactive Brokers, Alpaca, Binance |

## Event-Driven Architecture

The core of QF-Lib is an event loop managed by `EventManager`:

```mermaid
sequenceDiagram
    participant EM as EventManager
    participant Timer
    participant Notifiers
    participant Strategy
    participant AlphaModel
    participant PositionSizer
    participant Broker
    participant Portfolio

    loop While continue_trading
        EM->>Timer: Get next event time
        Timer->>EM: TimeEvent (MarketClose)
        EM->>Notifiers: dispatch_next_event()
        Notifiers->>Strategy: on_market_close()
        Strategy->>AlphaModel: calculate_exposure()
        AlphaModel-->>Strategy: Signal
        Strategy->>PositionSizer: size_position(Signal)
        PositionSizer->>Broker: place_order(Order)
        Broker->>Portfolio: update_positions(Fill)
        Portfolio->>EM: PortfolioEvent
    end
    EM->>Portfolio: end_of_trading_update()
```

## Class Hierarchy

### Alpha Model Framework

```mermaid
classDiagram
    class AlphaModel {
        <<abstract>>
        +risk_estimation_factor: float
        +data_provider: AbstractPriceDataProvider
        +get_signal(ticker, current_exposure, current_time, frequency) Signal
        +calculate_exposure(ticker, current_exposure, current_time, frequency)* Exposure
        +calculate_fraction_at_risk(ticker, current_time, frequency) float
    }

    class FuturesModel {
        +calculate_exposure()
        +calculate_fraction_at_risk()
    }

    class RandomTradesAlphaModel {
        +calculate_exposure()
    }

    class Exposure {
        <<enum>>
        LONG
        SHORT
        OUT
    }

    class Signal {
        +ticker: Ticker
        +suggested_exposure: Exposure
        +fraction_at_risk: float
        +last_available_price: float
        +creation_time: datetime
        +alpha_model: AlphaModel
    }

    AlphaModel <|-- FuturesModel
    AlphaModel <|-- RandomTradesAlphaModel
    AlphaModel --> Signal : creates
    Signal --> Exposure : contains
```

### Trading Session Builder Pattern

```mermaid
classDiagram
    class TradingSession {
        <<abstract>>
        +settings: Settings
        +data_provider: DataProvider
        +broker: Broker
        +monitor: AbstractMonitor
        +event_manager: EventManager
        +start_trading()
    }

    class BacktestTradingSession {
        +start_date: datetime
        +end_date: datetime
    }

    class BacktestTradingSessionBuilder {
        +set_frequency()
        +set_backtest_name()
        +set_alpha_model()
        +set_position_sizer()
        +build() BacktestTradingSession
    }

    TradingSession <|-- BacktestTradingSession
    BacktestTradingSessionBuilder --> BacktestTradingSession : builds
```

### Data Provider Abstraction

```mermaid
classDiagram
    class DataProvider {
        <<abstract>>
        +timer: Timer
        +get_history(tickers, fields, start, end, frequency)*
        +get_last_available_price(tickers, frequency, end_time)
        +supported_ticker_types()*
    }

    class AbstractPriceDataProvider {
        <<abstract>>
        +get_price(tickers, fields, start, end, frequency)
    }

    class PresetDataProvider {
        +data: QFDataArray
    }

    class PrefetchingDataProvider {
        +wrapped_provider: DataProvider
        +cached_data: dict
    }

    class BloombergDataProvider
    class InteractiveBrokersDataProvider
    class AlpacaDataProvider
    class BinanceDataProvider
    class YFinanceDataProvider
    class CSVDataProvider

    DataProvider <|-- AbstractPriceDataProvider
    AbstractPriceDataProvider <|-- PresetDataProvider
    AbstractPriceDataProvider <|-- PrefetchingDataProvider
    AbstractPriceDataProvider <|-- BloombergDataProvider
    AbstractPriceDataProvider <|-- InteractiveBrokersDataProvider
    AbstractPriceDataProvider <|-- AlpacaDataProvider
    AbstractPriceDataProvider <|-- BinanceDataProvider
    AbstractPriceDataProvider <|-- YFinanceDataProvider
    AbstractPriceDataProvider <|-- CSVDataProvider
```

## Portfolio Construction Architecture

```mermaid
graph LR
    subgraph "Input"
        RET[Historical Returns] --> COV_EST[Covariance Estimator]
        VIEWS[Investor Views] --> BL[Black-Litterman]
    end

    subgraph "Covariance Estimation"
        COV_EST --> SAMPLE[Sample Covariance]
        COV_EST --> SHRINK[Shrinkage Estimator]
        COV_EST --> EXPO[Exponential Covariance]
    end

    subgraph "Optimization"
        SAMPLE --> QO[Quadratic Optimizer]
        SHRINK --> QO
        EXPO --> QO
        BL --> QO
        QO --> |min variance| W1[Weights]
        QO --> |max Sharpe| W2[Weights]
        QO --> |risk parity| W3[Weights]
    end
```

## Custom Container Types

QF-Lib provides typed containers that extend pandas:

| Container | Base | Purpose |
|-----------|------|---------|
| `QFSeries` | `pd.Series` | General financial time series |
| `QFDataFrame` | `pd.DataFrame` | Multi-column financial data |
| `QFDataArray` | `xarray.DataArray`-like | 3D data (date x ticker x field) |
| `PricesSeries` | `QFSeries` | Price data with domain validation |
| `ReturnsSeries` | `QFSeries` | Returns data |
| `LogReturnsSeries` | `QFSeries` | Log returns |
| `SimpleReturnsSeries` | `QFSeries` | Simple returns |

## Key Architectural Decisions

1. **Event-driven over vectorized**: The backtesting engine is event-driven to accurately simulate real trading conditions including order latency, partial fills, and market impact.

2. **Builder pattern for sessions**: `BacktestTradingSessionBuilder` allows flexible configuration of backtests without complex constructor signatures.

3. **Abstract data provider**: A single interface across all data sources prevents vendor lock-in and simplifies strategy code.

4. **Look-ahead bias protection**: The `DataProvider.get_history()` method accepts a `look_ahead_bias` flag that, when False, ensures no future data leaks into the backtest.

5. **Timer abstraction**: `Timer` (with `RealTimer` and `SettableTimer` implementations) enables the same code to run in both backtest and live modes.

6. **Separation of alpha and sizing**: Alpha models produce exposure signals (LONG/SHORT/OUT), while position sizers translate these into concrete order sizes, enforcing separation of concerns.

---
## See Also
- [README](README.md) — Project overview and quick start
- [Workflow](workflow.md) — Event flows and processing pipelines
- [State Management](state-management.md) — State lifecycle and data models
- [Development](development.md) — Development guide and best practices
