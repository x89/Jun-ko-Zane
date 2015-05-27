#!/usr/bin/env python

from juni import Juni
from time import sleep
from random import randint
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

@asyncio.coroutine
def fl_notifications():
    ws = yield from websockets.client.connect(wss_url)
    while True:
        msg = yield from ws.recv()
        print(msg)
        if not ws.open:
            break

# asyncio.get_event_loop().run_forever()
asyncio.get_event_loop().run_until_complete(fl_notifications())
