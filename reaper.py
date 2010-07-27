#!/usr/bin/env python
# encoding: utf-8

from PIL import Image
from PIL.ExifTags import TAGS
from geopy import geocoders

def get_lonlat(fn):
    """Get EXIF longitude/latitude data from a given image file."""
    t = {}
    i = Image.open(fn)
    for tag, value in i._getexif().items():
        t[TAGS.get(tag, tag)] = value
    if 'GPSInfo' in t:
        lat = \
            (t['GPSInfo'][2][0][0] / t['GPSInfo'][2][0][1]) + \
            (t['GPSInfo'][2][1][0] / t['GPSInfo'][2][1][1] / 60.0) + \
            (t['GPSInfo'][2][2][0] / t['GPSInfo'][2][2][1] / 3600.0)
        if t['GPSInfo'][1] == 'S':
            lat = -lat
        lon = \
            (t['GPSInfo'][4][0][0] / t['GPSInfo'][4][0][1]) + \
            (t['GPSInfo'][4][1][0] / t['GPSInfo'][4][1][1] / 60.0) + \
            (t['GPSInfo'][4][2][0] / t['GPSInfo'][4][2][1] / 3600.0)
        if t['GPSInfo'][3] == 'W':
            lon = -lon
        return (lat, lon)
    else:
        return None