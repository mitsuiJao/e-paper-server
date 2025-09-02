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
        self.draw.line(500, 0, 500, 480, 3)
        self.draw.line(0, 88, 500, 88, 3)
        return self.draw.to_bytes()
    
    def generate_glaph_image(self):
        pixel_width = 500
        pixel_height = 392
        dpi = 100
        figsize_width = pixel_width / dpi
        figsize_height = pixel_height / dpi

        fig1, ax1 = plt.subplots(figsize=(figsize_width, figsize_height), dpi=dpi)

        ax1.plot(self.weather_data["date"], self.weather_data["temperature"], marker="o", color="black")
        ax1.spines['right'].set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['left'].set_visible(False)
        ax1.tick_params(labelleft=True, left=False, labelbottom=True)
        ax1.xaxis.set_major_locator(mdates.HourLocator(interval=2))
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H'))

        path1 = "img/glaph1.png"
        plt.savefig(path1)

        fig2, ax2 = plt.subplots(figsize=(figsize_width, figsize_height), dpi=dpi)
        ax2.plot(self.weather_data["date"], self.weather_data["precipitation_probability"], marker="s", color="black")
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

    def draw_glaph(self):
        path1, path2 = self.generate_glaph_image()
        # path = "img/pose_galpeace_schoolgirl.png"
        self.draw.img(path1, -20, 100, 1, self.draw.BLACK)
        self.draw.img(path2, -20, 100, 1, self.draw.RED)
        return self.draw.to_bytes()


if __name__ == "__main__":
    w = DrawWeather()
    w.generate()
    w.draw._save("img/image.png")