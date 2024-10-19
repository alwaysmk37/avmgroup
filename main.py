from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles  # Import StaticFiles for serving static files
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load templates from the 'templates' directory (including the 'login' subdirectory)
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    # Render the index.html template
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/login")
async def login(request: Request):
    # Render the login.html template from the 'login' folder inside 'templates'
    return templates.TemplateResponse("login/login.html", {"request": request})

@app.get("/contact")
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/redirect_to_login")
async def redirect_to_login():
    # Redirect from index.html to login.html
    return RedirectResponse(url="/login")
