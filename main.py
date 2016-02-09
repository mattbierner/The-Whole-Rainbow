#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image
import requests
import json
from TwitterAPI import TwitterAPI

# Persisted data files
ROOT = os.path.dirname(os.path.realpath(__file__))
IMAGE_FILE = os.path.join(ROOT, 'color.png')
DATA_FILE = os.path.join(ROOT, 'color.data')

INITIAL_COLOR = 0x0
MAX_COLOR = 0xffffff

# Disable actual uploads
DEBUG = True

def int_rgb_tuple(num):
    return ((num >> 16) & 0xff, (num >> 8) & 0xff, num & 0xff)

def generate_image(color):
    """Create a solid image of color"""
    color_tuple = int_rgb_tuple(color)
    return Image.new('RGB', (500, 500), color=color_tuple)

def generate_image_file(color):
    """Create a file for a solid image of color"""
    img = generate_image(color)
    img.save(IMAGE_FILE)
    return IMAGE_FILE

def get_initial_color():
    """Get color to start with on boot"""
    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = f.readline()
            print data
            return int(data, base=16)
    else:
        return INITIAL_COLOR

def write_color_data(color):
    """Update persisted current color data"""
    with open(DATA_FILE, 'w') as f:
        f.write("{0:06x}".format(color))

def post_the_rainbow(start_color, api):
    """Try to post the next color and update state."""
    color = start_color
    if color > MAX_COLOR:
        print("Out of rainbow")
        return

    caption = "#{0:06x} #whole🌈".format(color)
    image_file = generate_image_file(color)

    if not DEBUG:
        with open(IMAGE_FILE, 'rb') as f:
            data = f.read()
        
        r = api.request('media/upload', None, {'media': data})
        if r.status_code != 200:
            print("Error uploading", color)
            return

        media_id = r.json()['media_id']
        r = api.request('statuses/update', {'status': caption, 'media_ids': media_id})
        if r.status_code != 200:
            print("Error posting", color)
            return

    color = color + 1
    write_color_data(color)

def arg_or_env(index, name):
    return sys.argv[1] if len(sys.argv) >= index else os.environ.get(name)

def main():
    consumer_key = arg_or_env(1, 'RAINBOW_TWITTER_CONSUMER_KEY')
    consumer_secret = arg_or_env(2, 'RAINBOW_TWITTER_CONSUMER_SECRET')
    token_key = arg_or_env(3, 'RAINBOW_TWITTER_ACCESS_TOKEN_KEY')
    token_secret = arg_or_env(4, 'RAINBOW_TWITTER_ACCESS_TOKEN_SECRET')

    intial_color = get_initial_color()
    api = TwitterAPI(consumer_key, consumer_secret, token_key, token_secret)
    post_the_rainbow(intial_color, api)


if __name__ == "__main__":
    main()
