# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
from twisted.enterprise import adbapi


class FirstSpiderPipeline(object):

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb',
            host = '127.0.0.1',
            db = 'lyh',
            user = 'root',
            passwd = '915348696',
            cursorclass = MySQLdb.cursors.DictCursor,
            charset = 'utf8',
            use_unicode = True)

    def process_item(self, item, spider):
        print spider
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tx, item):
        sql = "insert into yunbi (strike_time, price, amount) values (%s,%s,%s)"
        params = (item['strike_time'], item['price'], item['amount'])
        tx.execute(sql,  params)

    def handle_error(self, failue):
         print 'lyh %s' % failue
