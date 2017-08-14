# -*- coding: utf-8 -*-

# from scrapy import cmdline
#
#
# cmdline.execute('scrapy crawl yunbi -o info.csv -t csv'.split())

import time
import os

#定时运行
while True:
    os.system("scrapy crawl yunbi -o info.csv -t csv")
    time.sleep(300)