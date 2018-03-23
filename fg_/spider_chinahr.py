# coding=utf-8
'''抓取中华英才网，覆盖率需求'''
import csv
import re
import requests
import time

from zhinfo import *
from lxml import etree

class Chinahr(object):

    def __init__(self, city, pages, position_btitle, position, peer, company_name_list):
        self.city_str = ""
        self.position_str = ""
        self.peer = peer
        self.company_name_list=company_name_list
        self.city = CITY[city]
        self.position_btitle, self.position = self.inp_position(position_btitle, position)
        self.pages = pages
        self.num = 0
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        self.url = 'http://www.chinahr.com/%s/jobs/%s/'%(self.city,self.position)
        self.s = requests.session()
        self.s.get(url='http://www.chinahr.com/guangzhou/')

        self.position_info = []

    def spider(self):
        for i in range(1, int(self.pages)+1):
            url = self.url + '%s/' % i
            html = self.s.get(url=url,headers=self.headers).content.decode('utf-8')
            self.parse(html,i)
        self.save_csv(self.pages)
    def parse(self,html,pages):
        is_str = '对不起，没有找到满足条件的职位信息'
        if html.find(is_str) != -1:
            return
        selector = etree.HTML(html)
        node_list = selector.xpath('//div[@class="jobList"]')
        for node in node_list:
            self.num += 1 
            info_dict = {}
            Company = node.xpath('.//li[@class="l1"]//span[@class="e3 cutWord"]/a/text()')[0]
            # 判断是抓同行，还是抓本公司
            if self.peer:
                company = [self.peer, ]
            else:
                #company = MyCompany
                company=self.company_name_list
            if Company in company:
                title1 = node.xpath('.//li[@class="l1"]//span[@class="e1"]//a/text()')
                title2 = node.xpath('.//li[@class="l1"]//span[@class="e1"]//strong/text()')
                title = title1[0] if title1 else ""
                title_b = title2[0] if title2 else ""
                pub_time  = node.xpath('.//li[@class="l1"]//span[@class="e2"]/text()')[0]
                adderss = node.xpath('.//li[@class="l2"]//span[@class="e1"]/text()')[0]
                timer = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

                info_dict['职位名称'] = title + title_b
                info_dict['公司名称'] = Company
                info_dict['发布地址及要求'] = re.sub(r'[\r\t\n]?',"",adderss)
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
    
    def save_csv(self,pages):
        if not self.position_info:
            print('\n[INFO]: %s%s职位类别下的前(%s)页没有公司发布的职位信息\n' % (self.city_str, self.position_str, pages))
        else:
            filename = self.city_str + '_' + self.position_str.replace('/', "")
            if self.peer:
                filename = self.peer + '_' + self.position_str.replace('/', "") + '_同行' + '.csv'
            try:
                f = open('%s' % (filename + '.csv'), 'w',newline='')
            except Exception as e:
                f = open('%s' % (filename + '1.csv'), 'w', newline='')
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.position_info[0].keys())
            for item in self.position_info :
                csv_writer.writerow(item.values())
    def data(self):
        return self.position_info, self.num

def main():
    while True:
        global Peer, Peer_name
        print('\n1:抓取本公司覆盖率\n2:抓取同行覆盖率')
        serial_number = input('\n请输入编号选择：')
        Peer = False
        if serial_number == '2':
            Peer = True
            Peer_name = input("\n请输入同行名称：")
        chinahr = Chinahr()
        chinahr.spider()
        res = input("\n按回车继续,退出请输入q：")
        if res == 'q':
            break


if __name__ == "__main__":
    main()
