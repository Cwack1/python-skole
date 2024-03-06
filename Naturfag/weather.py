#pip install openmeteo-requests
#pip install requests-cache retry-requests numpy pandas matplotlib

#Henter median temperatur for hver dag fra 1990-01-01 til 2023-12-31
#Endre verdier her: https://open-meteo.com/en/docs/historical-weather-api/

#Dette kan brukes som utgangspunkt for å se på forskjeller i temperatur, nedbør og vind gjennom flere år
#
import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import matplotlib.pyplot as plt


# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 59.1312,
	"longitude": 10.2166,
	"start_date": "1990-01-01",
	"end_date": "2024-03-04",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean"],
	"timezone": "Europe/Berlin"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily.Variables(0).ValuesAsNumpy()
daily_data["temperature_2m_min"] = daily.Variables(1).ValuesAsNumpy()
daily_data["temperature_2m_mean"] = daily.Variables(2).ValuesAsNumpy()


#Graf
plt.plot(daily_data["date"], daily_data["temperature_2m_mean"])
plt.ylabel('Temperatur °C')
plt.xlabel('År')
plt.show()