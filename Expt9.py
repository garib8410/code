# ARIMA
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Sample time series data
data = [100, 120, 130, 140, 150, 160, 170, 180, 200, 210]
df = pd.Series(data)

# Fit ARIMA model
model = ARIMA(df, order=(1, 1, 1))
model_fit = model.fit()

# Forecast next values
forecast = model_fit.forecast(steps=3)

print("Forecasted Values:")
print(forecast)