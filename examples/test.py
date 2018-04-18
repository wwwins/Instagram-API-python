#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
import os
import sys

load_dotenv(verbose=True, dotenv_path='./.env')

api = InstagramAPI(os.getenv('USERNAME'), os.getenv('PASSWORD'))
if (api.login()):
    api.getSelfUserFeed()  # get self user feed
    print(api.LastJson)  # print last response JSON
    print("Login succes!")
else:
    print("Can't login!")
 
