from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .core.config import settings
from .routers import pages, websocket

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description="MliChat App - Aplikasi chat real time dan terenkripsi | Tugas Mata Kuliah Sistem Terdistribusi"
    )
    
    app.mount("/static", StaticFiles(directory="app/static"), name="static")
    
    app.include_router(pages.router)
    app.include_router(websocket.router)
    
    return app

app = create_app()
