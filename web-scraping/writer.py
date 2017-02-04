#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql.cursors

class Writer(object):

    # author ID for publishers.
    AUTHOR_ID = "1"

    SAVE_PATH = "/var/pti/scrape/{0}.txt"

    def __init__(self):
        user = os.environ.get('PTI_USER')
        password = os.environ.get('PTI_PASSWORD')
        host = os.environ.get('PTI_HOST')
        db = os.environ.get('PTI_DB')

        self.conn = pymysql.connect(user=user, password=password, host=host, database=database)

    def write(self, content):
        id = self._writeToDatabase(content)
        if id is None:
            return False

        self._writeToFile(id, content)

    def _writeToDatabase(self, content):
        ret = None
        with self.conn.cursor() as cur:
            cur.execute('SET NAMES utf8;')
            cur.execute('SET CHARACTER SET utf8;')
            cur.execute('SET character_set_connection=utf8;')
            sql = "INSERT INTO articles_articles(pub_date, url, author_id, title) VALUES (%s, %s, %s, %s)"
            r = cur.execute(sql, (content.pub_date, content.url, content.author_id, "dummy title"))
            ret = cur.lastrowid
            self.conn.commit()

        return ret

    def _writeToFile(self, id, content):
        path = self.SAVE_PATH.format(id)
        with io.FileIO(path, "w") as file:
            file.write(content)
