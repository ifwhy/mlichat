from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from ..services.crypto import crypto_service
from ..services.websocket_manager import manager

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/room/{room_id}", response_class=HTMLResponse)
async def chat_room(request: Request, room_id: str):
    return templates.TemplateResponse("chat.html", {
        "request": request,
        "room_id": room_id
    })


@router.get("/api/room/create")
async def create_room():
    room_id = crypto_service.generate_room_id()
    return {"room_id": room_id}


@router.get("/api/stats")
async def get_stats():
    return {
        "active_rooms": manager.get_active_rooms_count(),
        "total_peers": manager.get_total_peers_count()
    }
