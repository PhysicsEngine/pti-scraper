#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
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

  def clickByClassName(self, class_name):
    try:
      elem = self.driver.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, class_name)))
      ActionChains(self.driver).move_to_element(elem).click(elem).perform()
    except TimeoutException:
      raise ScrapingLibException("{0} class is not found".format(class_name))

  def get(self, url):
    self.driver.get(url)

  def get_latest_sorp(self):
    source = self.driver.page_source
    markup =  source.encode("utf-8")
    return self.create_soup(markup)

  def get_markup_by_driver(self, url):
    #print url
    self.driver.get(url)
    source = self.driver.page_source
    return source.encode("utf-8")

  def get_sorp(self, url, type = TYPE_DRIVER):
    markup = ""
    if(type == self.TYPE_DRIVER):
      markup = self.get_markup_by_driver(url)
    else:
      markup = self.get_markup_by_requests(url)
    return self.create_soup(markup)

  def get_latest_sorp(self):
    source = self.driver.page_source
    markup =  source.encode("utf-8")
    return self.create_soup(markup)

class ScrapingLibException(BaseException):
  pass

## test
if __name__ == '__main__':
  scraper = ScrapingLib()
  #print scraper.get_sorp("http://sumodb.sumogames.de/Results_text.aspx?b=201509&d=9")
