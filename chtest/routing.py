from channels import route
from chtest.consumers import ws_message, ws_connect, ws_disconnect

datastream = [
    route("websocket.receive", ws_message),
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
]
