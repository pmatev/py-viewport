import asyncio
from typing import Optional
from fastapi_websocket_pubsub import PubSubClient, PubSubEndpoint


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
        self.client = PubSubClient()

    async def __aenter__(self):
        # try to keep the connection open forever
        self.client.start_client(self.uri)
        await self.client.wait_until_ready()
        return self

    async def __aexit__(self, s, x, t):
        await self.client.disconnect()

    async def draw(self, img: bytes) -> None:
        await self.client.publish(['images'], data=img)
