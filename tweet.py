#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Twitter-Bot for FreiTux.

"""

from twython import Twython, TwythonError
import sys
import json
import time

APPNAME = 'twitterbot'
APPVERSION = '0.1'

def main():
    global apiKey, apiSecret, accessToken, accessTokenSecret, settings, api, tweet
    config_filename = 'twitter-config.json'
    try:
        with open(config_filename, 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError:
        print('Error: config file "{}" not found: {}'
              .format(config_filename))
        return
    except ValueError as e:
        print('Error: invalid config file "{}": {}'
              .format(config_filename, e))
        return
    apiKey = config.get('apiKey')
    if not apiKey:
        print('Error: config file doesn’t contain a `apiKey`')
        return
    apiSecret = config.get('apiSecret')
    if not apiSecret:
        print('Error: config file doesn’t contain a `apiSecret`')
        return
    accessToken = config.get('accessToken')
    if not accessToken:
        print('Error: config file doesn’t contain a `accessToken`')
        return
    accessTokenSecret = config.get('accessTokenSecret')
    if not accessTokenSecret:
        print('Error: config file doesn’t contain a `accessTokenSecret`')
        return
    tied = time.strftime("%H:%M")
    tweet = "Moinsens,\nick bün de FreiTux-Twitter-Bot\nnu is de Klock all " + tied + "."
    api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
    try:
        api.update_status(status=tweet)
    except TwythonError as e:
        print(e)

if __name__ == '__main__':
    main()
