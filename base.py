"""
Base routes for the API.

The routes in this module serve a very basic purpose, such as health checks and
version information.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pypacter_api import get_version
from test_version import detect_language

router = APIRouter()


@router.get("/health", tags=["health"])
async def health() -> JSONResponse:
    """
    Health check.

    Returns:
        A JSON response indicating the health of the API.
    """
    return JSONResponse(content={"status": "ok"})


@router.get("/version", tags=["version"])
async def version() -> JSONResponse:
    """
    Get the version of the API.

    Returns:
        A JSON response containing the version of the API.
    """
    return JSONResponse(content={"version": get_version()})


@router.post("/detect-language", tags=["language"])
async def detect_code_language(code_snippet: str) -> JSONResponse:
    """
    Detect the most likely programming language for a given code snippet.
    Parameters:
        - code_snippet (str): The input code snippet.
    Returns:
        A JSON response containing the detected programming language.
    """
    try:
        detected_language = detect_language(code_snippet)
        return JSONResponse(content={"detected_language": detected_language})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error detecting language: {str(e)}")
