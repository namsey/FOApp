import alpaca_trade_api as tradeapi
import pandas as pd

from config import API_KEY, API_SECRET, BASE_URL

# Set up Alpaca API client
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')


# Function to get real-time data from Alpaca
def get_real_time_data(symbol, start_date, end_date):
    barset = api.get_barset(symbol, 'minute', start=start_date, end=end_date)
    data = barset[symbol]

    # Convert to DataFrame
    df = pd.DataFrame({
        'time': [bar.t for bar in data],
        'open': [bar.o for bar in data],
        'high': [bar.h for bar in data],
        'low': [bar.l for bar in data],
        'close': [bar.c for bar in data],
        'volume': [bar.v for bar in data]
    })
    return df


# Example usage
if __name__ == '__main__':
    df = get_real_time_data('AAPL', '2023-09-12', '2023-09-13')
    print(df.head())
