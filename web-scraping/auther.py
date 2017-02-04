#!/usr/bin/env python
# -*- coding: utf-8 -*-
from db_uploader import DbUploader
class Author(object):
  def __init__(self):

  def __init__(self, conn, name, rate = 0):
    self.name = name
    self.rate = rate
    self.db_uploader = DbUploader(conn)
    self.author_id = get_authoer_id()

  def get_name(self):
    return self.name

  def get_rate(self):
    return self.rate

  def get_author_id(self):
    return self.author_id

  def get_authoer_id(self):
    auther_id = None
    try:

      
