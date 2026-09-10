"""Demand Planning & Forecasting simulation for SAP SCM/APO Week 1 project.

The dataset is simulated for educational purposes. The script compares:
1. Recursive 3-month moving average
2. Simple exponential smoothing (alpha=0.30, estimated initial level)
3. Multiplicative seasonal Holt-Winters (12-month seasonality, no trend)

Training period: Jan 2023-Dec 2024
Holdout period: Jan 2025-Jun 2025
"""

from pathlib import Path
import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing, SimpleExpSmoothing

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "demand_history.csv"


def recursive_moving_average(train, horizon=6, window=3):
    history = list(map(float, train))
    forecasts = []
    for _ in range(horizon):
        forecast = float(np.mean(history[-window:]))
        forecasts.append(forecast)
        history.append(forecast)
    return np.array(forecasts)


def simple_exponential_smoothing(train, horizon=6, alpha=0.30):
    model = SimpleExpSmoothing(
        train,
        initialization_method="estimated",
    ).fit(smoothing_level=alpha, optimized=False)
    return np.asarray(model.forecast(horizon), dtype=float)


def seasonal_holt_winters(train, horizon=6):
    model = ExponentialSmoothing(
        train,
        trend=None,
        seasonal="mul",
        seasonal_periods=12,
        initialization_method="estimated",
    ).fit(optimized=True)
    return np.asarray(model.forecast(horizon), dtype=float)


def metrics(actual, forecast):
    error = forecast - actual
    return {
        "MAE": np.mean(np.abs(error)),
        "RMSE": np.sqrt(np.mean(error ** 2)),
        "MAPE_percent": np.mean(np.abs(error / actual)) * 100,
        "Bias": np.mean(error),
    }


def main():
    df = pd.read_csv(DATA_FILE)
    demand = df["demand_units"].to_numpy(dtype=float)

    train = demand[:24]
    actual = demand[24:30]
    months = df["month"].iloc[24:30].to_numpy()
    horizon = len(actual)

    forecasts = {
        "3-Month Moving Average": recursive_moving_average(train, horizon=horizon),
        "Simple Exponential Smoothing": simple_exponential_smoothing(train, horizon=horizon, alpha=0.30),
        "Seasonal Holt-Winters": seasonal_holt_winters(train, horizon=horizon),
    }

    comparison = pd.DataFrame({"month": months, "actual": actual.astype(int)})
    metric_rows = []

    for name, forecast in forecasts.items():
        comparison[name] = np.round(forecast, 2)
        metric_rows.append({"model": name, **metrics(actual, forecast)})

    metric_df = pd.DataFrame(metric_rows)

    print("\nHoldout Forecast Comparison\n")
    print(comparison.to_string(index=False))
    print("\nAccuracy Metrics\n")
    print(metric_df.round(2).to_string(index=False))

    output_dir = ROOT / "results"
    output_dir.mkdir(exist_ok=True)
    comparison.to_csv(output_dir / "forecast_generated.csv", index=False)
    metric_df.round(4).to_csv(output_dir / "model_accuracy_generated.csv", index=False)

    best = metric_df.loc[metric_df["MAPE_percent"].idxmin()]
    print(f"\nBest model by MAPE: {best['model']} ({best['MAPE_percent']:.2f}%)")


if __name__ == "__main__":
    main()
