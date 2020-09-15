# -*- coding:utf-8 -*-
'''
IP代理池，设置操作数据库的类
	StrictRedis类连接数据库
		下面用到StrictRedis类里操作有序集合的相关方法：
			1、zadd(key,{member: score}):键key的集合添加权重score的元素member
			2、zscore(key,member):获取键key的集合中元素为member的权重
			3、zrangebyscore(key,min,max):返回键key的集合里权重在min和max之间的元素
			4、zrevrange(key,index1,index2):返回指定索引的元素，从高到低排列
			5、zincrby(key,increment, member)：给集合里指定的元素增加或减少权重
			6、zrem(key,member):移除集合里指定元素
			7、zcard(key):返回集合里元素个数

'''

MAX_SCORE = 100
MIN_SCORE = 0
INTTIAL_SCORE = 10
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_KEY = 'proxies'

import redis
from random import choice

class RedisClient(object):

	def __init__(self,host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD):
		'''初始化redis的地址、端口、密码'''

		self.db = redis.StrictRedis(host=host,port=port,password=password,
		decode_responses=True)

	def add(self, proxy, score=INTTIAL_SCORE):
		'''
		添加代理,设置初始化分数
		return：添加结果
		'''
		if not self.db.zscore(REDIS_KEY, proxy):
			return self.db.zadd(REDIS_KEY, {proxy: score})

	def random(self):
		'''
		随机获取有效代理，首先尝试获取最高分数代理，如果最高分数不存在，则按照排名获取，
		否则异常
		return：随机代理
		'''

		result = self.db.zrangebyscore(REDIS_KEY,MAX_SCORE,MAX_SCORE)
		if len(result):
			return choice(result)
		else:
			result = self.db.zrevrange(REDIS_KEY, 0, 100)
			if len(result):
				return choice(result)
			else:
				return repr('no proxy in proxypool')

	def decrease(self, proxy):
		"""
		代理值减一分，分数小于最小值时，代理删除
		return：修改后的代理分数
		"""
		score = self.db.zscore(REDIS_KEY,proxy)
		if score and score > MIN_SCORE:
			print('代理',proxy,'当前分数',score,'减1')
			return self.db.zincrby(REDIS_KEY, -1, proxy)
		else:
			print('代理',proxy,'当前分数',score,'移除')
			return self.db.zrem(REDIS_KEY, proxy)

	def exists(self,proxy):
	 	"""判断代理是否存在，返回是否存在"""
	 	return not self.db.zscore(REDIS_KEY,proxy) == None

	def max(self,proxy):
	 	'''将代理设置为MAX_SCORE'''
	 	print('代理',proxy,'可用，设置为',MAX_SCORE)
	 	return self.db.zadd(REDIS_KEY, {proxy: MAX_SCORE})

	def count(self):
		''' 获取代理数量,返回代理数量'''

		return self.db.zcard(REDIS_KEY)

	def all(self):
		'''获取全部代理，返回全部代理'''
		return self.db.zrangebyscore(REDIS_KEY,MIN_SCORE,MAX_SCORE)

	def b(self, proxy):
		self.db.zrem(REDIS_KEY, proxy)

if __name__ == '__main__':
	redis = RedisClient()
	print(redis.all())






























