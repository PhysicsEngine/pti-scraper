#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reuters_the_wire_scraper import ReutersTheWireScraper
from reuters_html2content import ReutersHtml2Content
from scraping_lib import ScrapingLib

if __name__ == '__main__':
    scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
    lib = ScrapingLib()
    html2content = ReutersHtml2Content()

    while True:
        for url in scraper.get_url_list():
            soup = lib.get_sorp(ReutersTheWireScraper.get_full_url(url))
            print html2content.parse(soup)

        # TODO: まずは最新のみ.
        break
