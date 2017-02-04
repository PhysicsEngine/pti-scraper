#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql.cursors

class DbConnect(object):

    def __init__(self):
        user = os.environ.get('PTI_USER')
        password = os.environ.get('PTI_PASSWORD')
        host = os.environ.get('PTI_HOST')
        database = os.environ.get('PTI_DB')
        conn = pymysql.connect(user=user, password=password, host=host, database=database)
        conn.encoding = "utf-8"
        self.conn = conn

    def get(self):
      return self.conn
