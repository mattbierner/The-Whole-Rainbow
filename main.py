#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from PIL import Image
import instagram
from cookielib import LWPCookieJar
import requests

ROOT = os.path.dirname(os.path.realpath(__file__))
IMAGE_FILE = os.path.join(ROOT, 'color.jpg')
DATA_FILE = os.path.join(ROOT, 'color.data')

INITIAL_COLOR = 0x0
MAX_COLOR = 0xffffff

# Disable actual uploads
DEBUG = False

username = None
if len(sys.argv) > 2:
    username = sys.argv[1]
else:
    username = os.environ.get('INSTAGRAM_USER_ID')

password = None
if len(sys.argv) > 2:
    password = sys.argv[2]
else:
    password = os.environ.get('INSTAGRAM_USER_PASSWORD')


def initial_sesion(force_update=False):
    """Get Instagram session"""
    s = requests.Session()
    s.cookies = LWPCookieJar('cookiejar')
    if force_update or not os.path.isfile('cookiejar'):
        session = instagram.InstagramSession(session=s)
        if not session.login(username, password):
            return None
        s.cookies.save()
        return session
    else:
        s.cookies.load(ignore_discard=True)
    return instagram.InstagramSession(session=s)

def int_rgb_tuple(num):
    return ((num >> 16) & 0xff, (num >> 8) & 0xff, num & 0xff)

def generate_image(color):
    """Create a solid image of color"""
    color_tuple = int_rgb_tuple(color)
    return Image.new('RGB', (500, 500), color=color_tuple)

def generate_image_file(color):
    """Create a file for a solid image of color"""
    img = generate_image(color)
    img.save(IMAGE_FILE, quality=100)
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

def post_the_rainbow(start_color, session):
    color = start_color
    if color > MAX_COLOR:
        print("Out of rainbow")
        return

    caption = "#{0:06x} #whole🌈".format(color)
    image_file = generate_image_file(color)

    if not DEBUG:
        media_id = session.upload_photo(image_file)
        if not media_id:
            print("Error uploading", color)
            return
        if not session.configure_photo(media_id, caption):
            print("Error posting", color)
            return

    color = color + 1
    write_color_data(color)

def main():
    intial_color = get_initial_color()
    session = initial_sesion()
    if initial_sesion is None:
        print("Error loging in to account")
        return
    post_the_rainbow(intial_color, session)

if __name__ == "__main__":
    main()
