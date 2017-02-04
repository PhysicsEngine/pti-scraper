#!/usr/bin/env python
# -*- coding: utf-8 -*-
from reuters_the_wire_scraper import ReutersTheWireScraper
from reuters_html2content import ReutersHtml2Content
from scraping_lib import ScrapingLib
from writer import Writer

if __name__ == '__main__':
    scraper = ReutersTheWireScraper(ReutersTheWireScraper.LOG_PATH)
    lib = ScrapingLib()
    html2content = ReutersHtml2Content()
    writer = Writer()

    while True:
        for url in scraper.get_url_list():
            soup = lib.get_sorp(ReutersTheWireScraper.get_full_url(url))
            content = html2content.parse(soup)
            writer.write(content)

        # TODO: まずは最新のみ.
        break
