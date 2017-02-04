#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Content(object):
    def __init__(self, author_id, text, url, pub_date, title):
        self.author_id = author_id
        self.text = text
        self.url = url
        self.pub_date = pub_date
        self.title = title


