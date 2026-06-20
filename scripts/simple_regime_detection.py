"""
Simple Regime Detection Example
This script demonstrates a basic way to detect market regimes
using moving average crossover. 
Useful as a foundation for more advanced regime detection systems.
"""

def detect_regime(prices, short_window=20, long_window=50):
    """
    Simple regime detection using moving average crossover.
    
    Returns 'bullish', 'bearish' or 'neutral' based on MA crossover.
    """
    if len(prices) < long_window:
        return "neutral (not enough data)"
    
    short_ma = sum(prices[-short_window:]) / short_window
    long_ma = sum(prices[-long_window:]) / long_window
    
    if short_ma > long_ma:
        return "bullish"
    elif short_ma < long_ma:
        return "bearish"
    else:
        return "neutral"


if __name__ == "__main__":
    # Example price data (replace with real data later)
    example_prices = [100, 102, 101, 105, 108, 107, 110, 115, 113, 118,
                      120, 119, 122, 125, 124, 128, 130, 129, 132, 135]
    
    regime = detect_regime(example_prices)
    
    print("Simple Regime Detection Example\n")
    print(f"Current detected regime: {regime.upper()}")
    print("\nThis is a basic example. Real systems use more indicators,")
    print("statistical methods, and machine learning for better accuracy.")
