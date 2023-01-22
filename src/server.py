from fastapi import FastAPI, WebSocket
from fastapi_websocket_pubsub import PubSubEndpoint

app = FastAPI()


@app.get("/")
def read_root():
    return {"todo": "return index.html"}


@app.websocket("/web")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        print(len(data))
        await websocket.send_text(f"received: {len(data)} bytes")

endpoint = PubSubEndpoint()

@app.websocket("/ws")
async def websocket_rpc_endpoint(websocket: WebSocket):
    await endpoint.main_loop(websocket)