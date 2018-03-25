
# coding=utf-8
'''抓取中华英才网，覆盖率需求'''
import csv
import requests
import time

from qcinfo import *
from lxml import etree

class Qiancheng(object):

    def __init__(self, city, pages, position_btitle, position, peer, company_name_list):
        self.city_str = city
        self.position_str = ""
        self.peer = peer
        self.company_name_list=company_name_list
        self.city = CITY[city]
        self.position_btitle, self.position = self.inp_position(position_btitle, position)
        self.pages = pages
        self.num = 0
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            "host":"www.51job.com"
        }
        self.url = 'http://search.51job.com/list/%s,000000,%s,00,9,99,%%2B,2,'%(self.city,self.position)
        
        self.s = requests.session()
        self.s.get(url='http://www.51job.com/',headers=self.headers)

        self.position_info = []

    def spider(self):
        for i in range(1, int(self.pages)+1):
            
            url = self.url + '%s.html?' % i
            print(url)
            html = self.s.get(url=url,headers=self.headers).content.decode('GBK')

            self.parse(html,i)
            
        self.save_csv(self.pages)
    def parse(self,html,pages):
        is_str = '对不起，没有找到符合你条件的职位！'
        if html.find(is_str)  != -1:
            return
        selector = etree.HTML(html)
        node_list = selector.xpath('//div[@class="dw_table"]/div[@class="el"]|//div[@class="dw_table"]/div[@class="el mk"]')
        for node in node_list:
            self.num += 1 
            info_dict = {}
            Company = node.xpath('.//span[@class="t2"]/a/@title')[0]
            # 判断是抓同行，还是抓本公司
            if self.peer:
                company = [self.peer, ]
            else:
                #company = MyCompany
                company=self.company_name_list
            if Company in company:
                title1 = node.xpath('.//p[@class="t1 "]/span/a/@title|.//p[@class="t1 tg1"]/span/a/@title')
                title = title1[0] if title1 else ""
                
                pub_time  = node.xpath('.//span[@class="t5"]/text()')[0]
                adderss = node.xpath('.//span[@class="t3"]/text()')[0]
                timer = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

                info_dict['职位名称'] = title
                info_dict['公司名称'] = Company
                info_dict["工作地点"] = adderss
                info_dict['抓取时间'] = timer
                info_dict['发布时间'] = pub_time
                info_dict['职位所在页'] = pages
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


if __name__ == "__main__":
    qc = Qiancheng('深圳', 3,'电子/电器/半导体/仪器仪表', '变压器与磁电工程师', None,company_name_list)
    qc.spider()
    a, b = qc.data()
    print(a, b)
