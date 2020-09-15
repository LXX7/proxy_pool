# -*- coding:utf-8 -*-

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = False
API_ENABLED = False

from multiprocessing import Process
from api import app
from getter import Getter
from tester import Tester
import time


class Scheduler():
	"""docstring for Scheduler"""
	def scheduler_tester(self, cycle=TESTER_CYCLE):
		tester = Tester()
		while True:
			print("测试器开始运行")
			tester.run()
			time.sleep(cycle)

	def scheduler_getter(self, cycle=GETTER_CYCLE):
		getter = Getter()
		while True:
			print("开始捉取代理")
			getter.run()
			time.sleep(cycle)

	def scheduler_api(self):
		app.run('localhost', 5555)
	
	def run(self):
		print('代理池开始运行')	
		if TESTER_ENABLED:
			tester_process = Process(target=self.scheduler_tester)
			tester_process.start()

		if GETTER_ENABLED:
			getter_process = Process(target=self.scheduler_getter)
			getter_process.start()

		if API_ENABLED:
			api_process = Process(target=self.scheduler_api)
			api_process.start()


if __name__ == '__main__':
	scheduler = Scheduler()
	scheduler.run()


