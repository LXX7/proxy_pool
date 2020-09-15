# -*- coding:utf-8 -*-
"""
主函数：可以获取代理IP，测试代理IP

1、修改测试地址，在tester.py里面修改：
    TEST_URL = 'http://www.baidu.com'

2、获取、测试、接口模块的开关，在scheduler.py里面修改：
    TESTER_ENABLED = True
    GETTER_ENABLED = True
    API_ENABLED = True

3、flask接口地址：
    http://localhost:5555/random接口里面可以获取随机可用的代理IP
    http://localhost:5555/count返回全部IP数目

4、添加新的可以爬取的代理IP网站：
    crawler.py可以添加爬取代理IP网站的方法，方法名以crawl_开头；方法最后返回yield ':'.join([ip, port])，例：123.163.117.132:9999

5、问题：flask里面如果可以添加点击获取IP就可以在网页里面操作观看可用IP地址

"""
from scheduler import Scheduler
from db import RedisClient

if __name__ == '__main__':

    # 获取redis数据库里面全部代理
    redis = RedisClient()
    print(redis.all())

    # 运行获取、测试、web接口模块
    scheduler = Scheduler()
    scheduler.run()
