# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from hhx_pool.items import HhxPoolItem
from redis import StrictRedis
import requests
class HhxPoolPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, HhxPoolItem):
            data = item['ip']+':'+item['port']
            # //判断是否能用
            # ip, port = (item['ip'], item['port'])
            # url = 'http://icanhazip.com'
            # proxy_url = "http://{0}:{1}".format(ip, port)
            # proxy_dict = {
            #     "http": proxy_url
            # }
            # response = requests.get(url, proxies=proxy_dict)
            # html_doc = str(response.content, 'gbk')
            # print('html_doc')
            # print(html_doc)
            # if html_doc ==item['ip']:
            redis = StrictRedis(host='localhost', port=6379, db=5, password='')
            redis.sadd(item['type'], data)
            return item

