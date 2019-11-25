import asyncio
from channels.consumer import AsyncConsumer


class ChatConsumer(AsyncConsumer):

    def websocket_connect(self, event):
        print('connection successful', event)