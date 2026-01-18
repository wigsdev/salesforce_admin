"""
Documentation API endpoints for markdown rendering.
"""

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.services.markdown_service import MarkdownService

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")
markdown_service = MarkdownService()


@router.get("/browse", response_class=HTMLResponse)
async def browse_docs(request: Request, path: str = ""):
    """
    Browse documentation directory.
    
    Args:
        request: FastAPI request
        path: Optional subdirectory path
        
    Returns:
        HTML page with directory listing
    """
    files = markdown_service.list_directory(path)
    
    return templates.TemplateResponse(
        "docs_browser.html",
        {
            "request": request,
            "files": files,
            "current_path": path,
            "title": "Documentation Browser"
        }
    )


@router.get("/{path:path}", response_class=HTMLResponse)
async def view_document(request: Request, path: str):
    """
    View a markdown document.
    
    Args:
        request: FastAPI request
        path: Path to markdown file
        
    Returns:
        HTML page with rendered markdown
        
    Raises:
        HTTPException: If document not found
    """
    document = markdown_service.get_document(path)
    
    if not document:
        raise HTTPException(
            status_code=404,
            detail=f"Document not found: {path}"
        )
    
    return templates.TemplateResponse(
        "doc_viewer.html",
        {
            "request": request,
            "title": document['title'],
            "html_content": document['html'],
            "toc": document['toc'],
            "path": document['path']
        }
    )
