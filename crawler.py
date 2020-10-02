# -*- coding:utf-8 -*-
'''
IP代理池，定义从不同代理网站爬取IP代理的类Crawler
'''

import requests
from pyquery import PyQuery as pq


class ProxyMetaclass(type):
	"""docstring for ProxyMetaclass"""
	def __new__(cls, name, bases, attrs):
		count = 0
		attrs['__CrawlFunc__'] = []
		for k,v in attrs.items():
			if 'crawl_' in k:
				attrs['__CrawlFunc__'].append(k)
				count +=1
		attrs['__CrawlFuncCount__'] = count
		return type.__new__(cls, name, bases, attrs)


class Crawler(object, metaclass=ProxyMetaclass):
	"""docstring for Crawler"""
	def get_proxies(self, callback):
		proxies = []
		for proxy in eval('self.{}()'.format(callback)):
			print('成功获取代理', proxy)
			proxies.append(proxy)
		return proxies

	def crawl_66ip(self, page_count=20):
		'''获取www.66ip.cn网站的代理'''
		start_url = 'http://www.66ip.cn/{}.html'
		urls = [start_url.format(page) for page in range(1, page_count+1)]
		for url in urls:
			print('crawling', url)
			html = requests.get(url)
			if html.status_code == 200:
				doc = pq(html.content.decode("GBK"))
				trs = doc('tr:gt(1)').items()
				for tr in trs:
					ip = tr.find('td:nth-child(1)').text()
					port = tr.find('td:nth-child(2)').text()
					yield ':'.join([ip, port])



if __name__ == '__main__':
	a = Crawler()
	a.crawl_66ip()






























