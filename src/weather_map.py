code_map = {
    "day": {
        0: "sun",
        1: "sun",
        2: "cloud_sun",
        3: "cloud_sun",
        45: "cloud",
        48: "cloud",
        51: "rain0_sun",
        53: "rain0_sun",
        55: "rain0_sun",
        56: "rain_snow",
        57: "rain_snow",
        61: "rain1_sun",
        63: "rain1_sun",
        65: "rain1_sun",
        66: "rain_snow",
        67: "rain_snow",
        71: "snow_sun",
        73: "snow_sun",
        75: "snow_sun",
        77: "snow_sun",
        80: "rain2",
        81: "rain2",
        82: "rain2",
        85: "rain_snow",
        86: "rain_snow",
        95: "rain_lightning",
        96: "rain_lightning",
        99: "rain_lightning"
    },
    "night": {
        0: "moon",
        1: "moon",
        2: "cloud_moon",
        3: "cloud_moon",
        45: "cloud",
        48: "cloud",
        51: "rain0",
        53: "rain0",
        55: "rain0",
        56: "rain_snow",
        57: "rain_snow",
        61: "rain1_moon",
        63: "rain1_moon",
        65: "rain1_moon",
        66: "rain_snow",
        67: "rain_snow",
        71: "snow_moon",
        73: "snow_moon",
        75: "snow_moon",
        77: "snow_moon",
        80: "rain2",
        81: "rain2",
        82: "rain2",
        85: "rain_snow",
        86: "rain_snow",
        95: "lightning",
        96: "lightning",
        99: "lightning",
    }
}


string_map = {
    "晴": "sun",
    "曇": "cloud",
    "雨": "rain",
    "雪": "snow",
    "霧": "cloud",
    "雷雨": "lightning",
    "風雪強い": "wind",
    "大雨": "rain",
    "大雪": "snow",
    "暴風雨": "rain_lightning",
    "暴風雪": "rain_snow",
    "みぞれ": "rain_snow",
    "にわか雨": "rain"
}

"""
晴れ
晴時々曇
晴一時雨
晴時々雨
晴一時雪
晴時々雪
晴一時雨か雪
晴時々雨か雪
晴一時雨か雷雨
晴のち時々曇
晴のち曇
晴のち一時雨
晴のち時々雨
晴のち雨
晴のち一時雪
晴のち時々雪
晴のち雪
晴のち雨か雪
晴のち雨か雷雨
晴朝夕一時雨
晴朝の内一時雨
晴夕方一時雨
晴山沿い雷雨
晴山沿い雪
晴午のちは雷雨
晴昼頃から雨
晴夕方から雨
晴夜は雨
朝の内霧のち晴
晴明け方霧
晴朝夕曇
晴時々雨で雷を伴う
晴一時雪か雨
晴時々雪か雨
晴のち雪か雨
曇り
曇時々晴
曇一時雨
曇時々雨
曇一時雪
曇時々雪
曇一時雨か雪
曇時々雨か雪
曇一時雨か雷雨
霧
曇のち時々晴
曇のち晴
曇のち一時雨
曇のち時々雨
曇のち雨
曇のち一時雪
曇のち時々雪
曇のち雪
曇のち雨か雪
曇のち雨か雷雨
曇朝夕一時雨
曇朝の内一時雨
曇夕方一時雨
曇日中時々晴
曇昼頃から雨
曇夕方から雨
曇夜は雨
曇昼頃から雪
曇夕方から雪
曇夜は雪
曇海上海岸は霧か霧雨
曇時々雨で雷を伴う
曇時々雪で雷を伴う
曇一時雪か雨
曇時々雪か雨
曇のち雪か雨
雨
雨時々晴
雨時々止む
雨時々雪
雨か雪
大雨
暴風雨
雨一時雪
雨のち晴
雨のち曇
雨のち時々雪
雨のち雪
雨か雪のち晴
雨か雪のち曇
朝の内雨のち晴
朝の内雨のち曇
雨朝晩一時雪
雨昼頃から晴
雨夕方から晴
雨夜は晴
雨夕方から雪
雨夜は雪
雨一時強く降る
雨一時みぞれ
雪か雨
雨で雷を伴う
雪か雨のち晴
雪か雨のち曇
雪
雪時々晴
雪時々止む
雪時々雨
大雪
風雪強い
暴風雪
雪一時雨
雪のち晴
雪のち曇
雪のち雨
朝の内雪のち晴
朝の内雪のち曇
雪昼頃から雨
雪夕方から雨
雪一時強く降る
雪のちみぞれ
雪一時みぞれ
雪で雷を伴う
"""