import numpy as np
from scipy.stats import norm


# Black-Scholes model for options pricing
def black_scholes(price, strike, time, volatility, rate, option_type='call'):
    d1 = (np.log(price / strike) + (rate + 0.5 * volatility ** 2) * time) / (volatility * np.sqrt(time))
    d2 = d1 - volatility * np.sqrt(time)

    if option_type == 'call':
        price = (price * norm.cdf(d1)) - (strike * np.exp(-rate * time) * norm.cdf(d2))
    elif option_type == 'put':
        price = (strike * np.exp(-rate * time) * norm.cdf(-d2)) - (price * norm.cdf(-d1))

    return price
