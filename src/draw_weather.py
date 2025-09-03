import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from PIL import ImageOps
from datetime import datetime, timedelta
import re

from draw import Draw
import requestAPI
import xbm2img
from weather_map import code_map, string_map

class DrawWeather():
    def __init__(self):
        self.draw = Draw()
        self.weather_data = requestAPI.get_weather()
        now = datetime.now()
        self.start = now.strftime("%Y-%m-%d %H:00")
        self.end = (now + timedelta(days=1)).strftime("%Y-%m-%d %H:00")
        self.use_data = self.weather_data[self.weather_data["date"].between(self.start, self.end)]
        print(self.weather_data)

    def generate(self):
        self.draw_glaph_field()
        self.draw.line(500, 0, 500, 480, 3)
        self.draw.line(0, 88, 500, 88, 3)
        return self.draw.to_bytes()
    
    def generate_glaph_image(self):
        pixel_width = 500
        pixel_height = 385
        dpi = 100
        figsize_width = pixel_width / dpi
        figsize_height = pixel_height / dpi

        fig1, ax1 = plt.subplots(figsize=(figsize_width, figsize_height), dpi=dpi)

        ax1.plot(self.use_data["date"], self.use_data["temperature"], marker="o", color="black")
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        ax1.tick_params(labelleft=True, left=False, labelbottom=True)
        ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H'))

        path1 = "img/glaph1.png"
        plt.savefig(path1)

        fig2, ax2 = plt.subplots(figsize=(figsize_width, figsize_height), dpi=dpi)
        ax2.plot(self.use_data["date"], self.use_data["precipitation_probability"], marker="s", color="black")
        ax2.set_ylim(0, 100)
        ax2.yaxis.tick_right()
        ax2.spines['right'].set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['left'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        ax2.tick_params(bottom=False, left=False, right=False, top=False, labelbottom=False)
        path2 = "img/glaph2.png"
        plt.savefig(path2)

        return path1, path2

    def draw_glaph_field(self):
        path1, path2 = self.generate_glaph_image()
        # path = "img/pose_galpeace_schoolgirl.png"
        self.draw.img_path(path1, -20, 107, 1, self.draw.BLACK)
        self.draw.img_path(path2, -20, 107, 1, self.draw.RED)
        x = 50
        for i in range(4):
            ind = int(self.use_data.iloc[i*8]["weather_code"])
            nightdayflg = ""
            if 6 < self.use_data.iloc[i*8]["date"].hour < 18:
                nightdayflg = "day"
            else:
                nightdayflg = "night"
            self.draw.img_pil(ImageOps.invert(xbm2img.xbm2img(f"img/32/{code_map[nightdayflg][ind]}.xbm")), x, 90, 2)
            x += 108
        
        self.draw.text("C", 14, 108, 2)
        self.draw.text("%", 446, 108, 2, self.draw.RED)

        return self.draw.to_bytes()

    def draw_info_field(self):
        weather_str = requestAPI.get_weather_summary()

    def _purser_weather(self, weather):
        del_word = ["海上海岸", "を伴う", "朝夕", "夕方", "山沿い", "朝のうち", "明け方"]

if __name__ == "__main__":
    w = DrawWeather()
    w.generate()
    w.draw._save("img/image.png")