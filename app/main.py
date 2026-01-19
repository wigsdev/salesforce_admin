"""
Main FastAPI application.

This module initializes the FastAPI app and configures middleware, routers, and static files.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from app.config import settings

# Create FastAPI application
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="Interactive learning platform for Salesforce Admin certification",
    debug=settings.DEBUG
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configure Jinja2 templates
templates = Jinja2Templates(directory="app/templates")




@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy"}


# Include routers
from app.routers import auth, users, docs, progress, frontend

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(docs.router, prefix="/docs", tags=["Documentation"])
app.include_router(progress.router, prefix="/api/progress", tags=["Progress"])
app.include_router(frontend.router, tags=["Frontend"])

# TODO: Include other routers when created
# from app.routers import sprints
# app.include_router(sprints.router, prefix="/api/sprints", tags=["sprints"])
