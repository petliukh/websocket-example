"""
ASGI config for websocket_example project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""


import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from live_calculator import routing as lc_routing
from web_clock import routing as wc_routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "websocket_example.settings")

application = ProtocolTypeRouter({
"http": get_asgi_application(),
"websocket": AuthMiddlewareStack(
		URLRouter(
			lc_routing.websocket_urlpatterns +
            wc_routing.websocket_urlpatterns
		),
	),
})
