import requests
import urllib.parse
import openmeteo_requests
import pandas as pd
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry

def request_API(url, **kwargs):
    requestURL = url
    requestURL += "?"
    for key in kwargs.keys():
        requestURL += key
        requestURL += "="
        requestURL += urllib.parse.quote(kwargs[key])
        
    res = requests.get(requestURL)
    if res.status_code == 200:
        dirdate = res.json()
    else:
        return
    
    res.close()

    return dirdate

def get_weather():
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 35.48938557,
        "longitude": 133.80834793,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "hourly": ["temperature_2m", "precipitation_probability", "rain", "weather_code"],
        "forecast_days": 1,
    }

    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    hourly = response.Hourly()

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
    return hourly_dataframe


# print(get_weather())