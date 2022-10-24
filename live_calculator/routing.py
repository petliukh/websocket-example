from django.urls import path
from live_calculator import consumers


websocket_urlpatterns = [
	path(r'ws/livec/', consumers.Calculator.as_asgi()),
]
