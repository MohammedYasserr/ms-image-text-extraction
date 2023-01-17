import pathlib
import json
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# the directory where the app is(This method  gives us where the parent path is)
BASE_DIR = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get('/', response_class=HTMLResponse)  # http GET
def home_view(request: Request):
    print(request)
    return templates.TemplateResponse("home.html", {"request": request})


@app.post('/')  # http POST
def home_detail_view():
    return {"hello": "post"}


