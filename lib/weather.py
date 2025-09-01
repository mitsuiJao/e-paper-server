import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 35.48938557,
    "longitude": 133.80834793,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "hourly": ["temperature_2m", "precipitation_probability", "rain", "weather_code"],
    "timezone": "Asia/Tokyo",
    "forecast_days": 1,
}

# APIリクエストの実行
responses = openmeteo.weather_api(url, params=params)
response = responses[0]

# ---

### 時間別データ (Hourly)

hourly = response.Hourly()

# hourlyデータに必要な列を抽出
hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq="h",
        inclusive="left"
    ),
    "temperature": hourly.Variables(0).ValuesAsNumpy(),
    "precipitation_probability": hourly.Variables(1).ValuesAsNumpy(),
    "rain": hourly.Variables(2).ValuesAsNumpy(),
    "weather_code": hourly.Variables(3).ValuesAsNumpy(),
}

hourly_dataframe = pd.DataFrame(data=hourly_data)
fig, ax1 = plt.subplots(figsize=(12, 6))
ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

ax1.plot(hourly_dataframe["date"], hourly_dataframe["temperature"])
ax2 = ax1.twinx()
ax2.plot(hourly_dataframe["date"], hourly_dataframe["precipitation_probability"])
ax2.set_ylim(0, 100)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)

ax2.axis("off")

ax1.tick_params(labelleft=False, left=False, labelbottom=False)


plt.savefig("glaph.png")
print("\nHourly data\n", hourly_dataframe)