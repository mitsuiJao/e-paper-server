from fastapi import FastAPI
from fastapi.responses import Response
from draw_calendar import DrawCalendar

app = FastAPI()

@app.get("/")
async def root():
    return {"content": "Hello, World!"}

@app.get("/calendar")
async def send_calendar():
    c = DrawCalendar()
    bytes = c.generate()
    return Response(content=bytes, media_type="application/octet-stream")

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