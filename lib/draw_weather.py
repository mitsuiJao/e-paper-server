import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from draw import Draw
import requestAPI

class DrawWeather():
    def __init__(self):
        self.draw = Draw()
        self.weather_data = requestAPI.get_weather()

    def generate(self):
        self.draw_glaph()
        return self.draw.to_bytes()
    
    def generate_glaph_image(self):
        pixel_width = 500
        pixel_height = 392
        dpi = 100
        figsize_width = pixel_width / dpi
        figsize_height = pixel_height / dpi

        fig, ax1 = plt.subplots(figsize=(figsize_width, figsize_height), dpi=dpi)
        ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

        ax1.plot(self.weather_data["date"], self.weather_data["temperature"], marker="o", color="black")
        ax2 = ax1.twinx()
        ax2.plot(self.weather_data["date"], self.weather_data["precipitation_probability"], marker="s", color="black")
        ax2.set_ylim(0, 100)

        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)

        ax2.axis("off")

        ax1.tick_params(labelleft=False, left=False, labelbottom=False)

        path = "img/glaph.png"
        plt.savefig(path)
        return path

    def draw_glaph(self):
        path = self.generate_glaph_image()
        # path = "img/pose_galpeace_schoolgirl.png"
        self.draw.img(path)
        return self.draw.to_bytes()