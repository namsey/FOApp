# data/options_data.py

import pandas as pd
import requests

from config import API_KEY


# Function to get options data
def get_options_data(symbol, expiration_date):


# Example API endpoint for options data (replace with actual endpoint)
url = f'https://api.example.com/options/{symbol}?expiration={expiration_date}&api_key={API_KEY}'
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data['options'])
return df
