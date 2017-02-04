#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db_uploader import DbUploader
class Author(object):

  def __init__(self, conn):
    self.name = name
    self.db_uploader = DbUploader(conn)
    self.author_id = get_author_id()

  def get_name(self):
    return self.name

  def get_rate(self):
    return self.rate

  def get_author_id(self):
    return self.author_id

  def get_author_id(self):
    author_id = self.db_uploader.select_articles_authors(name)
    if author_id == None:
      return self.db_uploader.insert_articles_authors(name)
   
    return author_id
