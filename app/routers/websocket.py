from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ..services.websocket_manager import manager
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("MliChat")

router = APIRouter()

@router.websocket("/ws/{room_id}")
async def websocket_endpoint(websocket: WebSocket, room_id: str, name: str = "Anonymous"):
    room, peer_id = await manager.connect(room_id, websocket, name)
    logger.info(f"[CONNECT] User '{name}' joined room '{room_id}' with peer_id: {peer_id}")
    
    try:
        while True:
            data = await websocket.receive_json()
            message_type = data.get("type", "message")
            
            if message_type == "message":
                encrypted_content = data.get("content", "")
                sender_name = room.peer_names.get(peer_id, "Unknown")
                logger.debug(f"[MESSAGE] From: {sender_name} | Room: {room_id}")
                logger.debug(f"[ENCRYPTED] {encrypted_content[:80]}..." if len(encrypted_content) > 80 else f"[ENCRYPTED] {encrypted_content}")
                await room.broadcast_message(peer_id, encrypted_content)
            
            elif message_type == "typing":
                typing_data = {
                    "type": "typing",
                    "peer_id": peer_id,
                    "peer_name": room.peer_names.get(peer_id, "Unknown"),
                    "is_typing": data.get("is_typing", False)
                }
                for pid, ws in room.peers.items():
                    if pid != peer_id:
                        try:
                            await ws.send_json(typing_data)
                        except Exception:
                            pass
            
            elif message_type == "ping":
                await websocket.send_json({"type": "pong"})
    
    except WebSocketDisconnect:
        logger.info(f"[DISCONNECT] User '{name}' left room '{room_id}'")
        await manager.disconnect(room_id, peer_id)
    except Exception as e:
        logger.error(f"[ERROR] {e}")
        await manager.disconnect(room_id, peer_id)
