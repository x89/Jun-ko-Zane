#!/usr/bin/env python

from juni import Juni
from time import sleep
from random import randint
import json
import configparser
import asyncio
import websockets

config = configparser.ConfigParser()
config.read('juni.conf')

ids = (config.getint('DEFAULT', 'first_id'), config.get('DEFAULT', 'second_id'))
ids = (randint(100, 999), randint(100000, 999999))

j = Juni(ids)
wss_url = "wss://notifications.freelancer.com/{first_id}/{second_id}/websocket".format(
    first_id=ids[0],  # Turns out these are just random. 100-999
    second_id=ids[1],  # This can be a string, no reason not to only use int!
)

register_blob = b'{"channel":"auth","body":{"hash":"ccc5c539c16c344571bac1f39da804af","hash2":"GIwIMHaIGiESxa5xT0PzoOjA2uXY70UDsy5n95CDllw%3D","user_id":"14809114","channels":[4,13,16,30,31,33,116,150,215,254,270,301,336,421,564,568,588,590,619,620,622,667,683,698,711,741]}}'

@asyncio.coroutine
def fl_notifications():
    ws = yield from websockets.client.connect(wss_url)
    ws.send(register_blob)
    msg = yield from ws.recv()
    print(msg)
    msg = yield from ws.recv()
    print(msg)
    msg = yield from ws.recv()
    print(msg)

#asyncio.get_event_loop().run_forever()
asyncio.get_event_loop().run_until_complete(fl_notifications())
