import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("💉 COVID-19 Daily Vaccinations Forecast 📈")

# Load your cleaned dataset
df_vacc = pd.read_csv("country_vaccinations.csv")
df_vacc['date'] = pd.to_datetime(df_vacc['date'])

# Select country
country = st.selectbox("🌍 Select a country:", df_vacc['country'].unique())

# Filter data
df_country = df_vacc[df_vacc['country'] == country].copy()
df_country = df_country.sort_values('date')
df_country = df_country[['date', 'daily_vaccinations', 'total_vaccinations', 'people_vaccinated', 'people_fully_vaccinated']].dropna()

# Forecast period input
period = st.slider("⏳ Days to forecast:", 7, 60, 30)

# Feature engineering
df_country['days_since'] = (df_country['date'] - df_country['date'].min()).dt.days
df_country['day_of_week'] = df_country['date'].dt.dayofweek

# Prepare features and target
feature_cols = [
    'days_since',
    'total_vaccinations',
    'people_vaccinated',
    'people_fully_vaccinated',
    'day_of_week'
]
X = df_country[feature_cols]
y = df_country['daily_vaccinations']

# Fit linear regression model
model = LinearRegression()
model.fit(X, y)

# Prepare future features
last_row = df_country.iloc[-1]
future_dates = pd.date_range(df_country['date'].max() + pd.Timedelta(days=1), periods=period)
future_days_since = np.arange(df_country['days_since'].max() + 1, df_country['days_since'].max() + period + 1)
future_day_of_week = future_dates.dayofweek

# For simplicity, we'll assume the last known values for cumulative features
future_total_vaccinations = np.full(period, last_row['total_vaccinations'])
future_people_vaccinated = np.full(period, last_row['people_vaccinated'])
future_people_fully_vaccinated = np.full(period, last_row['people_fully_vaccinated'])

future_X = pd.DataFrame({
    'days_since': future_days_since,
    'total_vaccinations': future_total_vaccinations,
    'people_vaccinated': future_people_vaccinated,
    'people_fully_vaccinated': future_people_fully_vaccinated,
    'day_of_week': future_day_of_week
})

future_preds = model.predict(future_X)

# Combine actual and forecast
forecast_df = pd.DataFrame({
    'date': future_dates,
    'daily_vaccinations': future_preds
})

# Plot
fig, ax = plt.subplots()
ax.plot(df_country['date'], df_country['daily_vaccinations'], label='Actual 💉')
ax.plot(forecast_df['date'], forecast_df['daily_vaccinations'], label='Forecast 🔮', linestyle='--')
ax.set_xlabel('Date 📅')
ax.set_ylabel('Daily Vaccinations 💉')
ax.legend()
st.pyplot(fig)

# Show forecast data
st.subheader("🔢 Forecast data")
st.write(forecast_df)