#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import pymysql.cursors
import io
from db_uploader import DbUploader 

class Writer(object):

    # author ID for publishers.
    AUTHOR_ID = "1"

    SAVE_PATH = "/var/pti/scrape/{0}.txt"

    def __init__(self, conn):
        user = os.environ.get('PTI_USER')
        password = os.environ.get('PTI_PASSWORD')
        host = os.environ.get('PTI_HOST')
        database = os.environ.get('PTI_DB')
        self.conn = conn
        self.uploader = DbUploader(conn)

    def write_articles_file(self, content):
        content_id = self.uploader.select_articles_articles_by_url(content.url)
        if content_id is not None:
            return False
        articles_id = self.uploader.insert_articles_articles(content)
        if articles_id is None:
            return False

        self._write_wrticles_to_file(articles_id, content)
        return True

    def _write_wrticles_to_file(self, id, content):
        path = self.SAVE_PATH.format(id)
        with io.FileIO(path, "w") as file:
            file.write(content.text.encode('utf-8'))

    def replace_author(self, content):
        author_id = self.uploader.select_articles_authors(content.author_id)
        if author_id is None:
            author_id = self.uploader.insert_articles_authors(content.author_id)
        content.author_id = author_id
