from pathlib import Path
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
import logging

from viewport.proto.messages_pb2 import Action, InitCanvas

app = FastAPI()

logger = logging.getLogger(__name__)

FRONTEND_DIR = Path(__file__).parent / "frontend"


app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR / "build/static", html=True),
    name="root",
)


@app.route("/")
async def index(arg):
    return FileResponse(FRONTEND_DIR / "build/index.html")


@app.websocket("/viewport")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    action = Action(
        type=Action.INIT_CANVAS,
        init_canvas=InitCanvas(
            width=640,
            height=480,
            background="#FFFFFF",
            render_mode=InitCanvas.TWO_D,
        ),
    )

    await websocket.send_bytes(action.SerializeToString())

    while True:
        data = await websocket.receive_json()
        logger.info(data)
        await websocket.send_json({"status": "ok"})
