from fastapi import FastAPI
import google_calendar as gc
from misakifont import MisakiFont

app = FastAPI()

@app.get("/")
async def root():
    return {"content": "Hello, World!"}

@app.get("/events")
async def get_events():
    events = gc.get_calendar_events(gc.SERVICE_ACCOUNT_FILE, gc.CALENDAR_ID)
    return {"events": events}

@app.get("/font")
async def get_font(q=None):
    if len(q) != 1:
        return {"contsnts": "Bad Request"}
    mf = MisakiFont()    
    return {"bitmap": mf.font(ord(q))}