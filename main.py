from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Load templates from the 'templates' directory
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    # Render the login.html template
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/redirect_to_login")
async def redirect_to_login():
    # Redirect from index.html to login.html
    return RedirectResponse(url="/login")

