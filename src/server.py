from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

FRONTEND_DIR = Path(__file__).parent / 'frontend'


app.mount("/static", StaticFiles(directory=FRONTEND_DIR / 'build/static', html=True), name="root")

@app.route("/")
async def index(arg):
    return FileResponse(FRONTEND_DIR / 'build/index.html')


@app.websocket("/viewport")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    await websocket.send_json({'type': 'init'})

    while True:
        data = await websocket.receive_json()
        logger.info(data)
        await websocket.send_json({'status': 'ok'})
