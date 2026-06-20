"""
Main script for Crypto Regime Detection System
"""

from src.data_fetcher import fetch_crypto_prices, add_returns
from src.regime_detector import RegimeDetector
from src.alerts import AlertSystem
import matplotlib.pyplot as plt


def main():
    print("Starting Crypto Regime Detection System...")

    # 1. Fetch data from CoinGecko
    df = fetch_crypto_prices(symbol="bitcoin", days=90)
    if df is None:
        print("Could not fetch data.")
        return

    print(f"Fetched {len(df)} days of Bitcoin data")

    # 2. Calculate returns and volatility
    df = add_returns(df)

    # 3. Initialize and run regime detector
    detector = RegimeDetector(calm_threshold=0.02, crisis_threshold=0.05)
    df = detector.classify_time_series(df)
    summary = detector.get_regime_summary(df)

    # 4. Print regime distribution
    print("\nRegime distribution (last 90 days):")
    for regime, stats in summary.items():
        print(f"  {regime}: {stats['percentage']:.1f}% ({stats['count']} days)")

    # 5. Check for crisis signal
    signal = detector.detect_crisis_signal(df)
    if signal:
        print("\nActive warning: Market shows signs of stress!")
    else:
        print("\nNo critical alerts at the moment")

    # 6. Create and save regime plot
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["price"], label="Bitcoin Price", color="blue")
    plt.fill_between(df["date"], df["price"], alpha=0.3, color="green",
                     where=df["regime"] == "CALM", label="CALM Regime")
    plt.fill_between(df["date"], df["price"], alpha=0.3, color="yellow",
                     where=df["regime"] == "STRESSED", label="STRESSED Regime")
    plt.fill_between(df["date"], df["price"], alpha=0.3, color="red",
                     where=df["regime"] == "CRISIS", label="CRISIS Regime")
    plt.title("Bitcoin Regime Detection (90 days)")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig("regime_plot.png", dpi=150, bbox_inches="tight")
    print("\nPlot saved as 'regime_plot.png'")

    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()
