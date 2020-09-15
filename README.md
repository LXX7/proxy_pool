# proxy_pool
python实现代理IP池

代码可自定义：

1，修改测试地址，在tester.py里面修改：
    TEST_URL ='http://www.baidu.com'

2，获取，测试，接口模块的开关，在scheduler.py里面修改：
    TESTER_ENABLED = True
    GETTER_ENABLED = True
    API_ENABLED = True

3，flask接口地址：
    http：// localhost：5555 / random接口里面可以获取随机可用的代理IP
    http：// localhost：5555 / count返回全部IP数量

4，添加新的可以爬取的代理IP网站：
    crawler.py可以添加爬取代理IP网站的方法，方法名以crawl_开头；方法最后返回yield'：'。join（[ip，port]），例：123.163.117.132：9999

