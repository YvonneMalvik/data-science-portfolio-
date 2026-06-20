"""
Crypto Data Fetcher - Henter historiske priser fra CoinGecko API
"""

import requests
import pandas as pd


def fetch_crypto_prices(symbol: str = "bitcoin", days: int = 90):
    """Henter daglig prisdata fra CoinGecko."""
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {"vs_currency": "usd", "days": days, "interval": "daily"}

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()["prices"]

        df = pd.DataFrame(data, columns=["timestamp", "price"])
        df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
        df = df[["date", "price"]]
        df = df.sort_values("date").reset_index(drop=True)

        return df

    except Exception as e:
        print(f"Feil ved henting av data: {e}")
        return None


def add_returns(df, period: int = 1):
    """Legger til avkastning og volatilitet."""
    df = df.copy()
    df["return_1d"] = df["price"].pct_change(period)
    df["volatility_5d"] = df["return_1d"].rolling(window=5).std()
    df["volatility_20d"] = df["return_1d"].rolling(window=20).std()
    return df.dropna()
