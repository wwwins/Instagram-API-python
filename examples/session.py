#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Save and load session
# session.py

from InstagramAPI import InstagramAPI
from dotenv import load_dotenv
from requests.cookies import cookiejar_from_dict
from pathlib import Path
import os
import sys
import pickle

load_dotenv(verbose=True, dotenv_path='./.env')
api = InstagramAPI(os.getenv('USERNAME'), os.getenv('PASSWORD'))

def genSessionObj(obj):
    return {
        'token': obj.token,
        'username_id': obj.username_id,
        'rank_token': obj.rank_token,
        'uuid': obj.uuid,
        'session': obj.s.cookies.get_dict(),
        'device_id': obj.device_id
    }

def saveSession(apiObj):
    with open('session.pkl','wb') as f:
        print('Save session.pkl')
        pickle.dump(genSessionObj(apiObj), f)

def loadSession():
    if Path('session.pkl').is_file():
        with open('session.pkl', 'rb') as f:
            print('Load session.pkl')
            load_session = pickle.load(f)
            api.token = load_session['token']
            api.username_id = load_session['username_id']
            api.rank_token = load_session['rank_token']
            api.uuid = load_session['uuid']
            api.s.cookies = cookiejar_from_dict(load_session['session'])
            api.device_id = load_session['device_id']
            api.isLoggedIn = True
    else:
        api.isLoggedIn = False

# relogin
loadSession()
if (api.isLoggedIn is not True):
    if (api.login()):
        api.getSelfUserFeed()  # get self user feed
        print(api.LastJson)  # print last response JSON
        print("Login success!!")
        saveSession(api)
    else:
        print("Can't login!")
else:
    if(api.isLoggedIn):
        print("reLogin success!!!")
        api.getSelfUserFeed()
        print(api.LastJson)
