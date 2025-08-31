from fastapi import FastAPI
from fastapi.responses import Response
from draw_calendar import DrawCalendar

app = FastAPI()
c = DrawCalendar()

@app.get("/")
async def root():
    return {"content": "Hello, World!"}

@app.get("/calendar")
async def send_calendar(color:str, part:int):
    if not 0 <= part < 1:
        return Response(status_code=400)
    black_bytes, red_bytes = c.generate()

    part_height = 480 // 2
    part_size = 800 * part_height // 8

    start = part * part_size
    end = start + part_size

    if color == "black":
        data_bytes = black_bytes[start:end]
    elif color == "red":
        data_bytes = red_bytes[start:end]
    else:
        return Response(status_code=400)

    return Response(content=data_bytes, media_type="application/octet-stream")

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