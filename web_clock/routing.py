from django.urls import path
from web_clock import consumers


websocket_urlpatterns = [
	path(r'ws/web-clock-live/', consumers.WebClock.as_asgi()),
]
