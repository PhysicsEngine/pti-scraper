#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scraping_lib import ScrapingLib
from bs4 import BeautifulSoup
from selenium import webdriver
from content import Content
import requests
import os
import pytz
from datetime import datetime

class ReutersHtml2Content(object):
    def parse(self, full_url, soup):
        return Content(
                "1",
                "\n".join(map(lambda x: x.text, soup.find_all("p"))),
                full_url,
                self.parse_time(self.get_revision_date(soup)),
                soup.title.string)

    def get_author_name(self, soup):
        for tag in soup.find_all("meta"):
            if tag.get("name", None) == "DCSext.rAuthor":
                return tag.get("content", None)
        return "unknown"

    def get_revision_date(self, soup):
        for tag in soup.find_all("meta"):
            if tag.get("name", None) == "REVISION_DATE":
                return tag.get("content", None)
        return "2017-02-04 11:22:33" # fuck

    def parse_time(self, tstr):
        try:
            # ex) "Fri Feb 03 10:56:58 UTC 2017"
            return datetime.strptime(tstr, "%a %b %d %H:%M:%S %Z %Y").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Tokyo'))
        except ValueError:
            # ex) "2017-02-03T10:56:58+0000"
            return datetime.strptime(tstr, "%Y-%m-%dT%H:%M:%S%z").astimezone(pytz.timezone('Asia/Tokyo'))
        raise ValueError

## test
if __name__ == '__main__':
    scraper = ScrapingLib()
    html2content = ReutersHtml2Content()
    url = "http://jp.reuters.com/article/idJP2017020301002019?sp=true"
    soup = scraper.get_sorp(url);
    print html2content.parse(url, soup)

