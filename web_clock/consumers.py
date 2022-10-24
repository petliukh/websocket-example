import asyncio
from datetime import datetime
from channels.generic.websocket import AsyncConsumer, json


class WebClock(AsyncConsumer):
    async def websocket_connect(self, event):
        self.connected = True
        print("connected", event)
        await self.send({
            "type": "websocket.accept"
        })

        while self.connected:
            await asyncio.sleep(0.1)
            await self.send({
                'type': 'websocket.send',
                'text': json.dumps({'current_time': str(datetime.now())}),
            })

    async def websocket_receive(self, event):
        print("receive", event)

    async def websocket_disconnect(self, event):
        print("disconnected", event)
        self.connected
