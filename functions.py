import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib
import plotly.graph_objects as go
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def regression_report(Y, y_pred):
    mae = mean_absolute_error(Y, y_pred)
    mse = mean_squared_error(Y, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(Y, y_pred)
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

def predict_curve(X, stock):
    model = joblib.load(f'./pkls/LinearRegression_{stock}.pkl')
    scaler = joblib.load(f'./pkls/scaler_{stock}.pkl')
    X_scaled = scaler.transform(X)
    Y_pred = model.predict(X_scaled)
    return Y_pred

def plot_last_30_days(column_name):
    last_30_days = joblib.load(f'./pkls/first_30_days_{column_name}.pkl')
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=last_30_days.index, y=last_30_days.values,
                             mode='lines+markers', name=column_name))
    fig.update_layout(title=f'Last 30 Days of {column_name}',
                      xaxis_title='Date',
                      yaxis_title=f'{column_name} (CAD)',
                      xaxis_rangeslider_visible=True)
    fig.show()

def predict_curve_7_days(column_name):
    X = joblib.load(f'./pkls/linear_test_{column_name}.pkl')
    X.index = X.index + pd.DateOffset(days=7)
    today_value = joblib.load(f'./pkls/todayvalue_{column_name}.pkl')
    Y_pred = predict_curve(X, column_name)
    values = []
    for i in range(len(Y_pred)):
        values.append(today_value)
        today_value += Y_pred[i]
    fig = go.Figure([go.Scatter(x=X.index, y=values)])
    fig.update_layout(title=f'Next 7 Days of {column_name}',
                      xaxis_title='Date',
                      yaxis_title=f'{column_name} (CAD)',
                      xaxis_rangeslider_visible=True)
    fig.show()

def regression_training(stock):
    data = joblib.load(f'./pkls/linear_{stock}.pkl')
    
    X = np.array(data.drop([f'{stock} Change'], axis=1))
    Y = np.array(data[f'{stock} Change'])

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    joblib.dump(scaler, f'./pkls/scaler_{stock}.pkl')

    model = LinearRegression()
    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    regression_report(Y_test, Y_pred)

    print('\n')

    joblib.dump(model, f'./pkls/LinearRegression_{stock}.pkl')