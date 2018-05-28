#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Login with session
# login_with_session.py

from session import Session

if __name__ == "__main__":
    sess = Session()
    sess.api.getSelfUserFeed()
    print(sess.api.LastJson)