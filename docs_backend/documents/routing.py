# documents/routing.py

from django.urls import re_path
from .consumers import DocumentConsumer  # Make sure this is your actual consumer class

websocket_urlpatterns = [
    re_path(r'ws/document/(?P<document_id>\w+)/$', DocumentConsumer.as_asgi()),  # Use as_asgi() to instantiate the consumer
]
