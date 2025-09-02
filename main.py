import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from fastapi import FastAPI
from fastapi.responses import Response
from draw_calendar import DrawCalendar
from draw_weather import DrawWeather


app = FastAPI()
c = DrawCalendar()
w = DrawWeather()
media_type = "application/octet-stream"

@app.get("/")
async def root():
    return {"content": "Hello, World!"}

@app.get("/calendar")
async def calendar():
    black_bytes, red_bytes = c.generate()
    c.draw._save("img/image.png")

    return Response(content=black_bytes+red_bytes, media_type=media_type)

@app.get("/weather")
async def weather():
    black_bytes, red_bytes = w.generate()
    w.draw._save("img/image.png")

    return Response(content=black_bytes+red_bytes, media_type=media_type)


# @app.get("/events")
# async def get_events():
#     events = gc.get_calendar_events(gc.SERVICE_ACCOUNT_FILE, gc.CALENDAR_ID)
#     return {"events": events}

# @app.get("/font")
# async def get_font(q=None):
#     if len(q) != 1:
#         return {"contsnts": "Bad Request"}
#     mf = MisakiFont()    
#     return {"bitmap": mf.font(ord(q))}