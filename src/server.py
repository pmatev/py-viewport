from fastapi import FastAPI, WebSocket
from fastapi_websocket_pubsub import PubSubEndpoint
import zmq
import zmq.asyncio

app = FastAPI()
context = zmq.asyncio.Context()
zmq_sock = context.socket(zmq.REP)


@app.on_event('startup')
def on_startup():
    zmq_sock.bind("tcp://127.0.0.1:11001")


@app.get("/")
def read_root():
    return {"todo": "return index.html"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print('handler start')
    await websocket.accept()
    print('handler accept')
    while True:
        print(f'waiting for zmq')
        data = await zmq_sock.recv()

        if isinstance(data, bytes):
            print('sending...')
            await websocket.send_bytes(data)

        # must reply to zmq socket to accept further requests
        await zmq_sock.send_string('ok')