from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import aiohttp

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/get_data")
async def get_data(request: Request, input1: str = Form(...), input2: str = Form(...)):
    async with aiohttp.ClientSession() as session:
        api_url = 'https://api.example.com/data'
        params = {'param1': input1, 'param2': input2}
        async with session.get(api_url, params=params) as response:
            data = await response.json()
            return data
