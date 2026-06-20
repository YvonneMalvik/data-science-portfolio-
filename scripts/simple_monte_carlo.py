"""
Simple Monte Carlo Simulation Example
This script demonstrates basic Monte Carlo simulation for price paths.
Useful as a starting point for more advanced trading strategy backtesting.
"""

import random
import statistics

def monte_carlo_simulation(initial_price=100, days=252, simulations=1000, volatility=0.02):
    """
    Run a simple Monte Carlo simulation of price paths.
    
    Args:
        initial_price: Starting price
        days: Number of trading days to simulate
        simulations: Number of different paths to generate
        volatility: Daily volatility (standard deviation)
    
    Returns:
        List of final prices from all simulations
    """
    final_prices = []
    
    for _ in range(simulations):
        price = initial_price
        for _ in range(days):
            # Random daily return (normal distribution)
            daily_return = random.gauss(0, volatility)
            price *= (1 + daily_return)
        final_prices.append(price)
    
    return final_prices


if __name__ == "__main__":
    print("Running Monte Carlo Simulation...\n")
    
    results = monte_carlo_simulation(
        initial_price=100,
        days=252,
        simulations=1000,
        volatility=0.02
    )
    
    mean_price = statistics.mean(results)
    median_price = statistics.median(results)
    min_price = min(results)
    max_price = max(results)
    
    print(f"Initial Price: 100")
    print(f"Number of Simulations: 1000")
    print(f"Trading Days: 252 (1 year)\n")
    
    print("Results after 1 year:")
    print(f"  Mean final price:   ${mean_price:.2f}")
    print(f"  Median final price: ${median_price:.2f}")
    print(f"  Min final price:    ${min_price:.2f}")
    print(f"  Max final price:    ${max_price:.2f}")
    print(f"\nThis is a simplified example. Real trading models use more advanced techniques.")
