#!/usr/bin/env python

from juni import Juni
import configparser

config = configparser.ConfigParser()
config.read('juni.conf')

ids = (config.getint('DEFAULT', 'first_id'), config.get('DEFAULT', 'second_id'))

j = Juni(ids)
kargs = {
        'somethings': 123,
        'somethingelse': 321,
        }

j.get(**kwargs)
