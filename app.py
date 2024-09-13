# app.py

from data.alpaca_data import get_real_time_data
from flask import Flask, jsonify, request

from data.futures_data import get_futures_data
from data.options_data import get_options_data
from models.lstm_model import prepare_data
from utils.data_utils import clean_data
from utils.options_utils import generate_options_signals

app = Flask(__name__)

# Load pre-trained LSTM model
model = None
scaler = None


@app.route('/')
def home():
    return "Financial Prediction App is running"


@app.route('/predict', methods=['GET'])
def predict():
    symbol = request.args.get('symbol', 'AAPL')
    start_date = request.args.get('start_date', '2023-09-12')
    end_date = request.args.get('end_date', '2023-09-13')

    # Get real-time data from Alpaca
    df = get_real_time_data(symbol, start_date, end_date)

    # Clean data
    df = clean_data(df)

    # Prepare data for LSTM model
    X_test, _, scaler = prepare_data(df)

    # Make prediction using LSTM model
    predicted_price = model.predict(X_test)
    predicted_price = scaler.inverse_transform(predicted_price)

    return jsonify({
        'symbol': symbol,
        'predicted_price': predicted_price[-1][0]
    })


@app.route('/futures', methods=['GET'])
def predict_futures():
    symbol = request.args.get('symbol', 'ES')
    start_date = request.args.get('start_date', '2023-09-12')
    end_date = request.args.get('end_date', '2023-09-13')

    df = get_futures_data(symbol, start_date, end_date)
    df = clean_data(df)

    # Future price predictions can be added here
    # Example: use LSTM or other models to predict futures prices

    return jsonify({
        'symbol': symbol,
        'data': df.to_dict(orient='records')
    })


@app.route('/options', methods=['GET'])
def predict_options():
    symbol = request.args.get('symbol', 'AAPL')
    expiration_date = request.args.get('expiration_date', '2023-09-30')

    option_data = get_options_data(symbol, expiration_date)
    signals = generate_options_signals(option_data)

    return jsonify({
        'symbol': symbol,
        'signals': signals
    })


if __name__ == '__main__':
    # Load and compile model
    from models.lstm_model import build_lstm_model

    model = build_lstm_model((60, 1))

    # Run Flask app
app.run(debug=True)
