#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Split an image into grid and upload images to instagram
#

from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
from PIL import Image
from time import sleep
from random import randint
import imageGrid
import os
import sys

if __name__ == "__main__":
    image_fn = sys.argv[1]
    div_x = int(sys.argv[2].split('x')[0])
    div_y = int(sys.argv[2].split('x')[1])

    load_dotenv(verbose=True, dotenv_path='./.env')
    api = InstagramAPI(os.getenv('USERNAME'), os.getenv('PASSWORD'))
    print('Start login!!')
    if (api.login()):
        print("Login success!!")
        for fn in imageGrid.saveGrid(image_fn, div_x, div_y):
            print("Upload {} file to ig".format(fn))
            sleep(randint(1,3))
            api.uploadPhoto(str(fn))
            print("Del {} file".format(fn))
            os.remove(str(fn))
    else:
        print("Can't login!")
 
