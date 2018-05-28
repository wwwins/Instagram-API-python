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

class Session:
    def __init__(self):
        load_dotenv(verbose=True, dotenv_path='./.env')
        self.api = InstagramAPI(os.getenv('USERNAME'), os.getenv('PASSWORD'))
        self.loadSession()
        if (self.api.isLoggedIn is not True):
            if (self.api.login()):
                print("Login success!!")
                self.saveSession(self.api)
            else:
                print("Can't login!")
        else:
            if(self.api.isLoggedIn):
                print("reLogin success!!!")


    def genSessionObj(self, obj):
        return {
            'token': obj.token,
            'username_id': obj.username_id,
            'rank_token': obj.rank_token,
            'uuid': obj.uuid,
            'session': obj.s.cookies.get_dict(),
            'device_id': obj.device_id
        }

    def saveSession(self, apiObj):
        with open('session.pkl','wb') as f:
            print('Save session.pkl')
            pickle.dump(self.genSessionObj(apiObj), f)

    def loadSession(self):
        if Path('session.pkl').is_file():
            with open('session.pkl', 'rb') as f:
                print('Load session.pkl')
                load_session = pickle.load(f)
                self.api.token = load_session['token']
                self.api.username_id = load_session['username_id']
                self.api.rank_token = load_session['rank_token']
                self.api.uuid = load_session['uuid']
                self.api.s.cookies = cookiejar_from_dict(load_session['session'])
                self.api.device_id = load_session['device_id']
                self.api.isLoggedIn = True
        else:
            self.api.isLoggedIn = False

if __name__ == "__main__":
    sess = Session()
