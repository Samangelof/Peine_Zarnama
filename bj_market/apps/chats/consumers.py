# myapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'lobby'
        self.room_group_name = f'chat_{self.room_name}'

        # Присоединение к комнате
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Приветствие нового пользователя
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': f'{self.scope["user"]} has joined the chat'
            }
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Отсоединение от комнаты
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        # Уведомление о выходе пользователя
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': f'{self.scope["user"]} has left the chat'
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Отправка сообщения в комнату
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': f'{self.scope["user"]}: {message}'
            }
        )

    async def chat_message(self, event):
        message = event['message']

        # Отправка сообщения клиенту
        await self.send(text_data=json.dumps({
            'message': message
        }))
