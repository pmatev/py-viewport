import os
from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
import zmq
import zmq.asyncio

app = FastAPI()
context = zmq.asyncio.Context()
zmq_sock = context.socket(zmq.REP)


@app.on_event('startup')
def on_startup():
    zmq_sock.bind("tcp://127.0.0.1:11001")


app.mount("/", StaticFiles(directory="frontend/build", html=True), name="root")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await zmq_sock.recv()

        if isinstance(data, bytes):
            await websocket.send_bytes(data)

        # must reply to zmq socket to accept further requests
        await zmq_sock.send_string('ok')