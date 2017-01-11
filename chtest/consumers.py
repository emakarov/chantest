import json

from django.http import HttpResponse

from channels import Channel, Group
from channels.handler import AsgiHandler
from channels.sessions import channel_session
from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http

def channel_send(channel, data):
    channel.send({
        'text': json.dumps(data)
    })

def group_send(kind, data):
    data = {
        'kind': kind,
        'data': data
    }
    print('sending data to websocket', data)
    channel_send(Group(kind), data)

def ws_connect(message):
    Group("location_update").add(message.reply_channel)
    channel_send(message.reply_channel, {'accept': True})
    group_send('location_update', {'msg': 'connected'})

def ws_disconnect(message):
    Group("location_update").discard(message.reply_channel)
    print('disconnected')

def ws_message(message):
    group_send('location_update', {'msg': 'got message on server'})
