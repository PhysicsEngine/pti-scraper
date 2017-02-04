#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time

class ScrapingLib(object):
  TYPE_DRIVER = "driver"
  TYPE_REQUESTS = "requests"
  PHANTOMJS_ARGS = ['--ignore-ssl-errors=true']

  def __init__(self, log_path = os.path.devnull):
    self.driver = webdriver.PhantomJS(service_args=self.PHANTOMJS_ARGS, service_log_path=log_path) 
    self.driver.wait = WebDriverWait(self.driver, 5)

  @classmethod
  def create_soup(cls, markup):
    return BeautifulSoup(markup, "html5lib")

  @classmethod
  def get_markup_by_requests(cls, url):
    res = requests.get(url)
    return res.text.encode(res.encoding)

  def get_markup_by_driver(self, url):
    print url
    self.driver.get(url)
    print self.driver.current_url
    source = self.driver.page_source
    return source.encode("utf-8")

  def get_sorp(self, url, type = TYPE_DRIVER):
    markup = ""
    if(type == self.TYPE_DRIVER):
      markup = self.get_markup_by_driver(url)
    else:
      markup = self.get_markup_by_requests(url)
    return self.create_soup(markup)

## test
if __name__ == '__main__':
  scraper = ScrapingLib()
  print scraper.get_sorp("http://sumodb.sumogames.de/Results_text.aspx?b=201509&d=9")
