from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chats
from .consumers import ChatConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/', ChatConsumer.as_asgi()),
]
