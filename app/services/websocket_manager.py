import json
import uuid
from datetime import datetime
from typing import Dict, Set
from fastapi import WebSocket


class Room:
    def __init__(self, room_id: str):
        self.room_id = room_id
        self.peers: Dict[str, WebSocket] = {}
        self.peer_names: Dict[str, str] = {}
        self.created_at = datetime.now()
    
    async def add_peer(self, peer_id: str, websocket: WebSocket, display_name: str):
        self.peers[peer_id] = websocket
        self.peer_names[peer_id] = display_name
        await self.broadcast_peer_list()
        await self.broadcast_system_message(f"{display_name} bergabung ke room")
    
    async def remove_peer(self, peer_id: str):
        if peer_id in self.peers:
            display_name = self.peer_names.get(peer_id, "Unknown")
            del self.peers[peer_id]
            if peer_id in self.peer_names:
                del self.peer_names[peer_id]
            await self.broadcast_system_message(f"{display_name} meninggalkan room")
            await self.broadcast_peer_list()
    
    async def broadcast_message(self, sender_id: str, encrypted_message: str):
        sender_name = self.peer_names.get(sender_id, "Unknown")
        message_data = {
            "type": "message",
            "sender_id": sender_id,
            "sender_name": sender_name,
            "content": encrypted_message,
            "timestamp": datetime.now().isoformat()
        }
        await self._broadcast(message_data, exclude=None)
    
    async def broadcast_system_message(self, message: str):
        message_data = {
            "type": "system",
            "content": message,
            "timestamp": datetime.now().isoformat()
        }
        await self._broadcast(message_data)
    
    async def broadcast_peer_list(self):
        peer_list = [
            {"id": pid, "name": name}
            for pid, name in self.peer_names.items()
        ]
        message_data = {
            "type": "peer_list",
            "peers": peer_list,
            "count": len(peer_list)
        }
        await self._broadcast(message_data)
    
    async def _broadcast(self, data: dict, exclude: str = None):
        disconnected = []
        for peer_id, websocket in self.peers.items():
            if exclude and peer_id == exclude:
                continue
            try:
                await websocket.send_json(data)
            except Exception:
                disconnected.append(peer_id)
        
        for peer_id in disconnected:
            await self.remove_peer(peer_id)
    
    @property
    def peer_count(self) -> int:
        return len(self.peers)
    
    def is_empty(self) -> bool:
        return self.peer_count == 0


class ConnectionManager:
    def __init__(self):
        self.rooms: Dict[str, Room] = {}
    
    def get_or_create_room(self, room_id: str) -> Room:
        if room_id not in self.rooms:
            self.rooms[room_id] = Room(room_id)
        return self.rooms[room_id]
    
    def get_room(self, room_id: str) -> Room | None:
        return self.rooms.get(room_id)
    
    def remove_room(self, room_id: str):
        if room_id in self.rooms:
            del self.rooms[room_id]
    
    def generate_peer_id(self) -> str:
        return str(uuid.uuid4())[:8]
    
    async def connect(self, room_id: str, websocket: WebSocket, display_name: str) -> tuple[Room, str]:
        await websocket.accept()
        room = self.get_or_create_room(room_id)
        peer_id = self.generate_peer_id()
        await room.add_peer(peer_id, websocket, display_name)
        
        await websocket.send_json({
            "type": "connected",
            "peer_id": peer_id,
            "room_id": room_id,
            "display_name": display_name
        })
        
        return room, peer_id
    
    async def disconnect(self, room_id: str, peer_id: str):
        room = self.get_room(room_id)
        if room:
            await room.remove_peer(peer_id)
            if room.is_empty():
                self.remove_room(room_id)
    
    def get_active_rooms_count(self) -> int:
        return len(self.rooms)
    
    def get_total_peers_count(self) -> int:
        return sum(room.peer_count for room in self.rooms.values())


manager = ConnectionManager()
