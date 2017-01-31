from channels import route
from .consumers import ws_connect, ws_receive, ws_disconnect, new_chat, new_notice, start_poll, result_poll

websocket_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.receive", ws_receive),
    route("websocket.disconnect", ws_disconnect),
]

# Websocket command :
custom_routing = [
    route("talk.receive", new_chat, command="^chat$"),
    route("talk.receive", new_notice, command="^notice$"),
    route("talk.receive", start_poll, command="^start_poll$"),
    route("talk.receive", result_poll, command="^result_poll$"),
]