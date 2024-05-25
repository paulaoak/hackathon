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
async def get_data(input1: str = Form(...), input2: str = Form(...)):
    result = print("This paper will help you")
    return {"result": result}
    
@app.post("/sum")
async def calculate_sum(input1: str = Form(...), input2: str = Form(...)):
    result = print("This paper will help you")
    return {"sum": result}