import requests
import urllib.parse

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

# YEAR = 2025
# s = f"https://holidays-jp.github.io/api/v1/{YEAR}/date.json"
# print(request_API(s))