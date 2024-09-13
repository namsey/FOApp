import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.models import Sequential


# Function to prepare data for LSTM
def prepare_data(df, time_step=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(df['close'].values.reshape(-1, 1))

    X_train, y_train = [], []
    for i in range(time_step, len(scaled_data)):
        X_train.append(scaled_data[i - time_step:i, 0])
        y_train.append(scaled_data[i, 0])

    X_train = np.array(X_train)
    y_train = np.array(y_train)

    # Reshape for LSTM model input
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    return X_train, y_train, scaler


# Build LSTM model
def build_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))  # Output layer (predicting price)

    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


# Example usage
if __name__ == '__main__':
    from data.alpaca_data import get_real_time_data

    df = get_real_time_data('AAPL', '2023-09-12', '2023-09-13')
    X_train, y_train, _ = prepare_data(df)
    model = build_lstm_model((X_train.shape[1], 1))
model.fit(X_train, y_train, epochs=1, batch_size=32)
print("Model training completed.")
