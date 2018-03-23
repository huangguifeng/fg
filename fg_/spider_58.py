# coding=utf-8
import requests
from info import City, position_dict
from lxml import etree
import csv
import time
import os 

base_path = os.path.dirname(os.path.abspath(__file__))

class SpiderTc():
    def __init__(self, page, peer, company_name_list):
        self.s = requests.session()
        self.pages = page
        self.peer = peer
        self.num = 0
        self.company_name_list = company_name_list
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36', 

        }
        self.info_list = []

    def my_spider(self):
        self.s.get(url='http://%s.58.com/' % self.city_url, headers=self.headers)
        self.is_page = True
        #from selenium import webdriver

       # from selenium.webdriver import DesiredCapabilities

        #driver=webdriver.PhantomJS(executable_path=base_path +'/phantomjs/bin/phantomjs.exe')

        #desired_capabilities= DesiredCapabilities.PHANTOMJS.copy()
       #desired_capabilities['phantomjs.page.customHeaders.User-Agent'] ='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'

        #driver= webdriver.PhantomJS(desired_capabilities=desired_capabilities)


        for i in range(1, int(self.pages) + 1):
            url='http://%s.58.com%spn%d/' % (self.city_url, self.position_type_url, i)
            response = self.s.get(
                url='http://%s.58.com%spn%d/' % (self.city_url, self.position_type_url, i), headers=self.headers)
            html = response.content.decode('utf-8')
            print(url)
            #driver.get(url)

            #html =  driver.page_source
            self.parse(html, i)
           
            # 当类别下没有任何职位，也就是无法获取到总页数。
            if not self.total_page:
                return
             #如果总页数大于请求页时，退出        
            if i >= int(self.total_page):
                return
            
    def parse(self, html, page):

        selector = etree.HTML(html)
        node_list = selector.xpath('//ul[@id="list_con"]//li')
        total = selector.xpath('//span[@class="operate_txt"]/i/text()')
        self.total = total[0] if total else ""
        total_page = selector.xpath('//i[@class="total_page"]/text()')
        self.total_page = total_page[0] if total_page else ""
        
        # 这个地方主要是用来判断，某个职位太少时，58自动推荐职位被抓取到
        if self.num >= int(self.total):
            return
        for node in node_list:
            # 除去精准的之后就是实际类别的职位
            if  not node.xpath('./a[@class="sign"]/text()'):
                self.num += 1
                
            info_dict = {}
            comp_names = node.xpath('.//div[@class="comp_name"]/a/@title')
            comp_name = comp_names[0] if comp_names else ""
            # 判断是抓同行，还是抓本公司
            if self.peer:
                company = [self.peer, ]
            else:
                company= self.company_name_list
            if comp_name in company:
                address = node.xpath('.//div[@class="job_name clearfix"]//span[1]/text()')
                comp_add = address[0] if address else ""
                position_titles = node.xpath('.//div[@class="job_name clearfix"]//span[2]/text()')
                position_title = position_titles[0] if position_titles else ""
                info_dict["公司名称"] = comp_name
                info_dict["职位地址"] = comp_add
                info_dict["职位名称"] = position_title
                info_dict["职位所在页"] = page
                info_dict['抓取时间'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                if self.is_page:
                    info_dict["职位总数"] = self.total
                    info_dict["职位总页数"] = self.total_page
                    self.is_page = False
                else:
                    info_dict["职位总数"] = ""
                    info_dict["职位总页数"] = ""
                #print(info_dict)
                self.info_list.append(info_dict)

    def save_csv(self):
        try:
            if not self.info_list:
                print('\n[INFO]: %s%s职位类别下的前(%s)页没有公司发布的职位信息\n' % (self.city, self.position_type, self.pages))
            else:
                file_name = self.city + self.position_type.replace('/', "") + '.csv'
                if self.peer:
                    file_name = self.peer + '_' + self.position_type.replace('/', "") + '_同行' + '.csv'
                with open(file_name, 'w', newline="") as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(self.info_list[0].keys())
                    for item in self.info_list:
                        csv_writer.writerow(item.values())
        except:
            print('ERROR 文件保存错误')

    def input_city(self, inp_city):
        address = City[inp_city]
        return address, inp_city

    def input_position(self, position_b_type, position_s_type):
        return position_dict[position_b_type][position_s_type], position_s_type


    def spiderTc(self,inp_city, position_b_type,position_s_type):
        self.city_url, self.city = self.input_city(inp_city)
        self.position_type_url, self.position_type = self.input_position(position_b_type,position_s_type)
        self.my_spider()
        self.save_csv()
        return self.info_list, self.num




