#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib

class DbUploader(object):
  def __init__(self, conn):
    self.conn = conn

  def insert_articles_articles(self, content):
    articles_id = None
    with self.conn.cursor() as cur:
      cur.execute('SET NAMES utf8;')
      cur.execute('SET CHARACTER SET utf8;')
      cur.execute('SET character_set_connection=utf8;')
      sql = "INSERT INTO articles_articles(pub_date, url, author_id, title) VALUES (%s, %s, %s, %s)"
      cur.execute(sql, (content.pub_date, content.url, content.author_id, content.title))
      articles_id = cur.lastrowid
      self.conn.commit()
  
    return articles_id

  def select_articles_authors(self, name):
    with self.conn.cursor() as cur:
      name_hash = self.name_hash(name)
      sql = "SELECT id FROM articles_authors where name_hash = '{0}'".format(name_hash)
      #print sql
      cur.execute(sql)
      return cur.fetchone()

  def insert_articles_authors(self, name):
    author_id = None
    with self.conn.cursor() as cur:
      cur.execute('SET NAMES utf8;')
      cur.execute('SET CHARACTER SET utf8;')
      cur.execute('SET character_set_connection=utf8;')
      sql = "INSERT INTO articles_authors(name, name_hash, rate) VALUES (%s, %s, %s)"
      cur.execute(sql, (name, self.name_hash(name), 0))
      author_id = cur.lastrowid
      self.conn.commit()
    return author_id

  def name_hash(self, name):
    return int(hashlib.md5(name.encode('utf-8')).hexdigest(), 16)
