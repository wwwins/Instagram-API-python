#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Split an image into grid and upload images to instagram with session
# upload_photo_grid_sess.py

from session import Session
from time import sleep
from random import randint
import imageGrid
import os
import sys

if __name__ == "__main__":
    image_fn = sys.argv[1]
    div_x = int(sys.argv[2].split('x')[0])
    div_y = int(sys.argv[2].split('x')[1])

    sess = Session()
    for fn in imageGrid.saveGrid(image_fn, div_x, div_y):
        print("Upload {} file to ig".format(fn))
        sleep(randint(1,3))
        sess.api.uploadPhoto(str(fn))
        print("Del {} file".format(fn))
        os.remove(str(fn))
