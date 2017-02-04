#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reuters_the_wire_scraper import ReutersTheWireScraper
from reuters_html2content import ReutersHtml2Content
from scraping_lib import ScrapingLib
from writer import Writer
from db_connect import DbConnect

# Usage:
# $ PTI_HOST=153.126.154.182 PTI_USER=pti PTI_PASSWORD=gussan_gologo13 PTI_DB=pti python2 app.py
if __name__ == '__main__':
    conn = DbConnect()
    scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
    lib = ScrapingLib()
    html2content = ReutersHtml2Content()
    writer = Writer(conn.get())

    while True:
        for url in scraper.get_url_list():
            full_url = ReutersTheWireScraper.get_full_url(url)
            soup = lib.get_sorp(full_url)
            content = html2content.parse(full_url, soup)
            writer.replace_author(content)
            writer.write_articles_file(content)
            scraper.load_more_content()
