# coding=utf-8

import requests
from lxml import etree
import csv
from gjinfo import *
import time


class GanJi(object):
    def __init__(self, city, pages, position_btitle, position, peer, company_name_list):
        self.city_str = ""
        self.position_str = ""
        self.city = CITY[city]
        self.position_btitle, self.position = self.inp_position( position_btitle, position)
        self.pages = pages
        self.position_info = []
        self.peer = peer
        self.num = 0
        self.company_name_list = company_name_list
        self.s = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }

    def spider(self):
        for i in range(1, int(self.pages) + 1):
            url = self.city + self.position + "o%s" % i
            html = self.s.get(url=url, headers=self.headers).text
            self.parse(html, i)
        self.save_csv(self.pages)

    def parse(self, html, pages):

        is_str = '没有更多了，为您推荐以下职位'
        if html.find(is_str) != -1:
            return
        selector = etree.HTML(html)
        node_list = selector.xpath('//div[@class="new-dl-wrapper"]//dl')

        for node in node_list:
            self.num += 1
            info_dict = {}
            company = node.xpath('.//div/a/@title')
            Company = company[0] if company else ""
            # 判断是抓同行，还是抓本公司
            if self.peer :
                company = [self.peer , ]
            else:
                company= self.company_name_list 
            if Company in company:
                title = node.xpath('.//dt//a/text()')
                title = title[0] if title else ""
                address = node.xpath('.//dd[@class="pay"]/text()')[0]
                pub_time = node.xpath('.//dd[@class="pub-time"]//span/text()')[0]
                timer = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                info_dict['职位名称'] = title
                info_dict['公司名称'] = Company
                info_dict['发布地址'] = address
                info_dict['抓取时间'] = timer
                info_dict['发布时间'] = pub_time
                info_dict['职位所在页'] = pages
                print(info_dict)
                self.position_info.append(info_dict)

    def inp_position(self, position_btitle, position):

            position_list = POSITION[position_btitle]
            self.position_str = position
            position = position_list[position]
            return position_btitle, position




    def save_csv(self, pages):
        if not self.position_info:
            print('\n[INFO]: %s%s职位类别下的前(%s)页没有公司发布的职位信息\n' % (self.city_str, self.position_str, pages))
        else:
            filename = self.city_str + '_' + self.position_str.replace('/', "")
            if self.peer :
                filename = self.peer  + '_' + self.position_str.replace('/', "") + '_同行'
            try:
                f = open('%s' % (filename + '.csv'), 'w', newline='')
            except Exception as e:
                f = open('%s' % (filename + '1.csv'), 'w', newline='')
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.position_info[0].keys())
            for item in self.position_info:
                csv_writer.writerow(item.values())
    def run(self):
        return self.position_info, self.num

