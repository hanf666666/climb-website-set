import requests
import scrapy
from scrapy import Request
from fake_useragent import UserAgent


"""
scrapy crawl kuaiproxy
"""
class KuaiproxySpider(scrapy.Spider):
    name = 'kuaiproxy'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/2/']
    headers = {
        'user-agent': UserAgent().random
    }
    test_url = 'http://httpbin.org/get'
    def parse(self, response):
        ips_list=response.xpath("//div[4]/div[2]/div[2]/div[2]/table//tr/td[1]/text()").extract()
        print(ips_list)
        ports_list=response.xpath("/html/body/div/div[4]/div[2]/div[2]/div[2]/table/tbody/tr/td[2]/text()").extract()
        for ip, port in zip(ips_list, ports_list):
            # 拼接ip与port
            proxy = ip.strip() + ":" + port.strip()
            # print(proxy)

            # 175.44.109.195:9999
            self.test_proxy(proxy)





    def test_proxy(self, proxy):
        '''测试代理IP是否可用'''
        proxies = {
            # 'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        # 参数类型
        # proxies
        # proxies = {'协议': '协议://IP:端口号'}
        # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=3)
            # 获取 状态码为200
            if resp.status_code == 200:
                print(proxy, '\033[31m可用\033[0m')
                # 可以的IP 写入文本以便后续使用
                # self.file.write(proxy)

            else:
                print(proxy, '不可用')

        except Exception as e:
            print(proxy, '不可用')
