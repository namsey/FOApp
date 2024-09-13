# data/futures_data.py

import pandas as pd
import requests

from config import API_KEY


# Function to get futures data
def get_futures_data(symbol, start_date, end_date):


# Example API endpoint for futures data (replace with actual endpoint)
url = f'https://api.example.com/futures/{symbol}?start={start_date}&end={end_date}&api_key={API_KEY}'
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data['prices'])
return df
