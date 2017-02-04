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
            full_url = ReutersTheWireScraper.get_full_url(url)
            soup = lib.get_sorp(full_url)
            content = html2content.parse(full_url, soup)
            writer.write(content)

        # TODO: まずは最新のみ.
        break
