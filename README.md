<p align="center">
  <img src="app/static/favicon.ico" alt="MliChat Logo" width="80" height="80">
</p>

<h1 align="center">MliChat</h1>

<p align="center">
  <strong>Secure Peer-to-Peer Real-time Chat Application with End-to-End Encryption</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/WebSocket-010101?style=for-the-badge&logo=socket.io&logoColor=white" alt="WebSocket">
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/uv-DE5FE9?style=for-the-badge&logo=uv&logoColor=white" alt="uv">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AES--256--GCM-Encrypted-00C853?style=flat-square" alt="Encryption">
  <img src="https://img.shields.io/badge/PBKDF2-Key%20Derivation-FF5722?style=flat-square" alt="PBKDF2">
  <img src="https://img.shields.io/badge/Real--time-WebSocket-2196F3?style=flat-square" alt="Real-time">
</p>

## Daftar Isi

- [Tentang Proyek](#tentang-proyek)
- [Fitur](#fitur)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Instalasi dan Setup](#instalasi-dan-setup)
  - [Menggunakan Docker](#menggunakan-docker-recommended)
  - [Tanpa Docker](#tanpa-docker-manual-setup)
- [Cara Penggunaan](#cara-penggunaan)
- [Struktur Proyek](#struktur-proyek)
- [Keamanan](#keamanan)
- [API Endpoints](#api-endpoints)

---

## Tentang Proyek

**MliChat** adalah aplikasi chat real-time yang menerapkan konsep sistem terdistribusi dengan arsitektur peer-to-peer melalui WebSocket. Aplikasi ini mengutamakan keamanan komunikasi dengan implementasi enkripsi end-to-end menggunakan algoritma **AES-256-GCM**.

Pesan yang dikirim antar pengguna dienkripsi di sisi client sebelum dikirim ke server, dan hanya dapat didekripsi oleh penerima yang berada di room yang sama. Server hanya bertindak sebagai relay dan tidak dapat membaca isi pesan.

> Video Dokumentasi Dapat Diakses [di sini](https://youtu.be/-zOa1pKPReQ).
---

## Fitur

| Fitur | Deskripsi |
|-------|-----------|
| **Real-time Messaging** | Komunikasi instan menggunakan WebSocket tanpa perlu refresh halaman |
| **End-to-End Encryption** | Pesan dienkripsi dengan AES-256-GCM, server tidak dapat membaca isi pesan |
| **Room-based Chat** | Buat atau bergabung ke room dengan kode unik 8 karakter |
| **Typing Indicator** | Indikator saat pengguna lain sedang mengetik |
| **Peer List** | Daftar peserta yang sedang online di room |
| **No Registration** | Tidak perlu login atau registrasi, langsung gunakan |
| **No Message Storage** | Pesan tidak disimpan di server maupun database |
| **Responsive Design** | Tampilan responsif untuk desktop, tablet, dan mobile |
| **Copy Room Code** | Salin kode room dengan satu klik untuk dibagikan |
| **Auto Reconnect** | Koneksi otomatis tersambung kembali jika terputus |

---


### Alur Komunikasi

1. **Client A** membuat pesan dan mengenkripsi dengan AES-256-GCM
2. Pesan terenkripsi dikirim melalui WebSocket ke **Server**
3. **Server** menerima pesan terenkripsi dan broadcast ke semua peer di room
4. **Client B** menerima pesan terenkripsi dan mendekripsi menggunakan key yang sama
5. Server tidak pernah melihat plaintext pesan

---

## Teknologi yang Digunakan

### Backend
| Teknologi | Versi | Deskripsi |
|-----------|-------|-----------|
| Python | 3.13 | Bahasa pemrograman utama |
| FastAPI | 0.115+ | Framework web async modern |
| Uvicorn | 0.32+ | ASGI server dengan dukungan WebSocket |
| WebSockets | 14.0+ | Library WebSocket untuk Python |
| Jinja2 | 3.1+ | Template engine untuk rendering HTML |
| Cryptography | 44.0+ | Library kriptografi (server-side utilities) |

### Frontend
| Teknologi | Deskripsi |
|-----------|-----------|
| HTML5 | Struktur halaman |
| Tailwind CSS | Utility-first CSS framework |
| JavaScript (ES6+) | Logika client-side |
| Web Crypto API | Enkripsi/dekripsi di browser |

### DevOps & Tools
| Teknologi | Deskripsi |
|-----------|-----------|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| uv | Fast Python package manager |
| GitHub Actions | CI/CD pipeline |
| Ruff | Python linter & formatter |
| Pytest | Testing framework |

---

## Instalasi dan Setup

### Prasyarat

- Python 3.13 atau lebih baru
- [uv](https://docs.astral.sh/uv/) package manager (recommended)
- Docker & Docker Compose (untuk setup dengan Docker)
- Git

---

### Menggunakan Docker (Recommended)

**1. Clone repository**

```bash
git clone https://github.com/username/MliChat.git
cd MliChat
```

**2. Jalankan dengan Docker Compose**

```bash
docker-compose up -d
```

**3. Akses aplikasi**

Buka browser dan akses: [http://localhost:8000](http://localhost:8000)

**4. Melihat logs**

```bash
docker-compose logs -f
```

**5. Menghentikan aplikasi**

```bash
docker-compose down
```

---

### Tanpa Docker (Manual Setup)

**1. Clone repository**

```bash
git clone https://github.com/username/MliChat.git
cd MliChat
```

**2. Install uv (jika belum)**

```bash
# Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**3. Install dependencies**

```bash
uv sync
```

**4. Jalankan aplikasi (Development)**

```bash
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**5. Jalankan aplikasi (Production)**

```bash
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

**6. Akses aplikasi**

Buka browser dan akses: [http://localhost:8000](http://localhost:8000)

---

### Menjalankan Tests

```bash
# Install dev dependencies
uv sync --dev

# Jalankan tests
uv run pytest -v

# Jalankan linter
uv run ruff check .

# Format code
uv run ruff format .
```

---

## Cara Penggunaan

### 1. Membuat Room Baru

1. Buka aplikasi di browser
2. Masukkan nama tampilan (Display Name)
3. Klik tombol **"Create New Room"**
4. Bagikan kode room kepada orang yang ingin diajak chat

### 2. Bergabung ke Room

1. Buka aplikasi di browser
2. Masukkan nama tampilan (Display Name)
3. Masukkan kode room yang diberikan
4. Klik tombol **"Join Room"**

### 3. Mengirim Pesan

1. Ketik pesan di kolom input
2. Tekan **Enter** atau klik tombol kirim
3. Pesan akan dienkripsi dan dikirim ke semua peserta di room

---

## Struktur Proyek

```
MliChat/
├── .github/
│   └── workflows/
│       └── ci.yaml              # GitHub Actions CI/CD
├── app/
│   ├── __init__.py
│   ├── main.py                  # FastAPI application entry point
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py            # Application configuration
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── pages.py             # HTML page routes
│   │   └── websocket.py         # WebSocket endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   ├── crypto.py            # Encryption utilities
│   │   └── websocket_manager.py # WebSocket connection manager
│   ├── static/
│   │   └── favicon.ico          # Application icon
│   └── templates/
│       ├── index.html           # Home page template
│       └── chat.html            # Chat room template
├── tests/
│   ├── __init__.py
│   └── test_app.py              # Application tests
├── .dockerignore                # Docker ignore file
├── .gitignore                   # Git ignore file
├── .python-version              # Python version specification
├── compose.yaml                 # Docker Compose configuration
├── Dockerfile                   # Docker build instructions
├── main.py                      # Alternative entry point
├── pyproject.toml               # Project dependencies & config
└── README.md                    # Project documentation
```

---

## Keamanan

### Enkripsi End-to-End

MliChat menggunakan **Web Crypto API** untuk enkripsi di sisi client:

| Komponen | Algoritma/Metode |
|----------|------------------|
| Key Derivation | PBKDF2 dengan 100,000 iterasi |
| Encryption | AES-256-GCM |
| Hash Function | SHA-256 |
| IV/Nonce | 12 bytes random per pesan |

### Bagaimana Cara Kerjanya?

1. **Key Derivation**: Kunci enkripsi diturunkan dari Room ID menggunakan PBKDF2
2. **Encryption**: Setiap pesan dienkripsi dengan AES-256-GCM menggunakan IV random
3. **Authentication**: GCM mode menyediakan authentication tag untuk integritas pesan
4. **Transmission**: Hanya ciphertext yang dikirim melalui WebSocket
5. **Decryption**: Client penerima mendekripsi menggunakan kunci yang sama

### Keamanan Server

- Server **tidak menyimpan** pesan apapun
- Server **tidak dapat membaca** isi pesan (hanya melihat ciphertext)
- Server hanya bertindak sebagai **relay** untuk meneruskan pesan terenkripsi
- Tidak ada database atau penyimpanan persisten

---

## API Endpoints

### HTTP Routes

| Method | Endpoint | Deskripsi |
|--------|----------|-----------|
| GET | `/` | Halaman utama (index) |
| GET | `/room/{room_id}` | Halaman chat room |
| GET | `/api/room/create` | Membuat room baru |

### WebSocket

| Endpoint | Deskripsi |
|----------|-----------|
| `ws://host/ws/{room_id}?name={display_name}` | Koneksi WebSocket ke room |

### WebSocket Message Types

**Client to Server:**
```json
{"type": "message", "content": "<encrypted_base64>"}
{"type": "typing", "is_typing": true}
{"type": "ping"}
```

**Server to Client:**
```json
{"type": "connected", "peer_id": "uuid"}
{"type": "message", "content": "<encrypted>", "sender_id": "uuid", "sender_name": "name", "timestamp": "iso8601"}
{"type": "system", "content": "User joined"}
{"type": "peer_list", "peers": [{"id": "uuid", "name": "name"}]}
{"type": "typing", "peer_id": "uuid", "peer_name": "name", "is_typing": true}
{"type": "pong"}
```

---

## Debug Mode

Untuk melihat log enkripsi/dekripsi di console FastAPI:

```bash
# Log akan menampilkan:
# [CONNECT] User 'name' joined room 'ABC123' with peer_id: uuid
# [MESSAGE] From: name | Room: ABC123
# [ENCRYPTED] base64_encrypted_content...
# [DISCONNECT] User 'name' left room 'ABC123'
```

---

## Lisensi

Proyek ini dibuat untuk keperluan tugas mata kuliah Sistem Terdistribusi.

---

<p align="center">
  Made with ❤️ by Ivan for Distributed Systems Course
</p>
