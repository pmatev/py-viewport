import zmq

class ViewportConnection:
    def __init__(self, ws) -> None:
        self.ws = ws

    async def __aexit__(self):
        pass

    async def __await__(self):
        pass


class Viewport:
    def __init__(self, uri = 'ws://localhost:3000/ws') -> None:
        self.uri: str = uri

    def __enter__(self):
        self.zmq_ctx = zmq.Context()
        self.zmq_sock = self.zmq_ctx.socket(zmq.REQ)
        self.zmq_sock.connect('tcp://127.0.0.1:11001')
        return self

    def __exit__(self, s, x, t):
        self.zmq_sock.close()

    def draw(self, img: bytes) -> None:
        self.zmq_sock.send(img)
