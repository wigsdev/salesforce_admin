from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    """
    Render the main dashboard page.
    """
    return templates.TemplateResponse("dashboard.html", {"request": request})


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """
    Render login page.
    """
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    """
    Render registration page.
    """
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/lumina/dashboard", response_class=HTMLResponse)
async def lumina_dashboard(request: Request):
    """
    Render the Lumina Tech Project Dashboard.
    """
    return templates.TemplateResponse(
        "lumina_dashboard.html",
        {
            "request": request,
            "title": "Dashboard Lumina Tech",
        },
    )
