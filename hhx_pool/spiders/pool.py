# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from hhx_pool.items import HhxPoolItem
from bs4 import BeautifulSoup
import random
# Headerk = {
#     "Host":"www.kuaidaili.com",
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Language":"zh-CN,zh;q=0.9",
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
# }
Headerx = {
    "Host":"www.xicidaili.com",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language":"zh-CN,zh;q=0.9",
    # "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
}
Proxy = [
    # '49.156.35.230:58113',
    # '176.113.116.70:55589',
    # '125.25.45.126:54662',
    # '86.123.166.109:8080',
    # '185.219.8.161:8080',
    # '91.146.251.138:8080',
    # '89.102.198.78:38412',
    # '185.67.191.75:34531',
    # '111.91.76.210:31089'
    '23.237.22.87:3128',
    '195.235.202.130:3128',
    '119.101.116.237:9999',
    '119.101.113.165:9999',
    '119.101.117.14:9999',
    '121.33.220.158:808',
    '119.123.173.82:9797'

]

class PoolSpider(scrapy.Spider):
    name = 'pool'
    # allowed_domains = ['https://www.kuaidaili.com','https://www.xicidaili.com']
    # start_urls = ['http://https://www.kuaidaili.com/']
    def start_requests(self):
        dicts=[
          # 'data_u',
          'xici'
        ]
        for dict in dicts:
            # if dict =='kuai':
            #     for i in range(1, 3):
            #         url ="https://www.kuaidaili.com/free/inha/"+str(i)+ "/"
            #         yield Request(url=url,callback=self.parse, meta ={'headers': Headerk,'proxy':'http://' + random.choice(Proxy),'type':dict})
            if dict =='xici':
                for i in range(4, 6):
                    url ="https://www.xicidaili.com/nn/"+str(i)
                    print(url)
                    yield Request(url=url,callback=self.parse, meta ={'headers': Headerx,'proxy':'http://' + random.choice(Proxy),'type':dict})



    def parse(self, response):
        print(response.status)
        poolItem = HhxPoolItem()
        soup = BeautifulSoup(response.text, "lxml")
        if response.meta['type']=='kuai':
            for ty in soup.find_all('tr'):
                if ty.select('td'):
                    ip = ty.select('td')[0].get_text()
                    port =ty.select('td')[1].get_text()
                    type = ty.select('td')[3].get_text()
                    poolItem['ip']=ip
                    poolItem['port'] = port
                    poolItem['type'] = type
                    print(poolItem)
                    yield poolItem
                    # return poolItem
        if response.meta['type']=='xici':
            for ul in soup.find_all("tr", class_="odd"):
                if ul.select('td'):
                    ip = ul.select('td')[1].get_text()
                    port = ul.select('td')[2].get_text()
                    type = ul.select('td')[5].get_text()
                    poolItem['ip'] = ip
                    poolItem['port'] = port
                    poolItem['type'] = type
                    print('your')
                    print(poolItem)
                    yield poolItem


