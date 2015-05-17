#!/usr/bin/env python

from juni import Juni
from time import sleep
import configparser
import asyncio
import websockets

config = configparser.ConfigParser()
config.read('juni.conf')

ids = (config.getint('DEFAULT', 'first_id'), config.get('DEFAULT', 'second_id'))

j = Juni(ids)
wss_url = "wss://notifications.freelancer.com/{first_id}/{second_id}/websocket".format(
    first_id=ids[0],
    second_id=ids[1],
)

@asyncio.coroutine
def fl_notifications():
    ws = yield from websockets.connect(wss_url)
    ret = yield from ws.recv()
    print(ret)


asyncio.get_event_loop().run_until_complete(fl_notifications())