# coding=utf-8
import requests
from zlinfo import position
from lxml import etree
import csv
import time


class SpiderZl(object):
    def __init__(self,company_name_list, peer=None):
        self.s = requests.session()
        self.peer = peer
        self.num = 0
        self.company_name_list = company_name_list
        self.headers = {
            "User-Agent": '"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36",'
        }
        self.position = []
        self.position_type = ""

    def request(self, bj, sj, pages, addr):
        for i in range(1, int(pages) + 1):
            url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?bj=%s&sj=%s&p=%s&jl=%s' % (bj, sj, i, addr)
            html = self.s.get(url, headers=self.headers).content
            self.parse(html, i)
        self.save_csv(addr, pages)

    def parse(self, html, page):
        is_exist = '以下职位也很不错，不妨试试'.encode('utf-8')
        if html.find(is_exist) != -1:
            return
        selector = etree.HTML(html)
        node_list = selector.xpath("//table[@class='newlist']")[1:]
        for node in node_list:
            self.num +=1
            position_dict = {}
            gsmc = node.xpath('.//td[@class="gsmc"]//a[1]/text()')
            gsmc = gsmc[0] if gsmc else ""
            # 判断是抓同行，还是抓本公司
            if self.peer:
                company = [self.peer, ]
            else:
                #company = MyCompany
                company=self.company_name_list
            if gsmc in company:
                zwmc = node.xpath('.//td[@class="zwmc"]//a/text()')
                zwmc = zwmc[0] if zwmc else ""
                gzdd = node.xpath('.//td[@class="gzdd"]/text()')
                gzdd = gzdd[0] if gzdd else ""
                position_dict['职位名称'] = zwmc
                position_dict['公司名称'] = gsmc
                position_dict['工作地点'] = gzdd
                position_dict['职位所在页'] = page
                position_dict['抓取时间'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

                self.position.append(position_dict)

    def save_csv(self, city, pages):
        if not self.position:
            print('\n[INFO]: %s%s职位类别下的前(%s)页没有公司发布的职位信息\n' % (city, self.position_type, pages))
        else:
            filename = city + '_' + self.position_type.replace('/', "")
            if self.peer:
                filename = self.peer + '_' + self.position_type.replace('/', "") + '_同行'
            try:
                f = open('%s' % (filename + '.csv'), 'w', encoding='utf-8', newline='')
            except Exception as e:
                f = open('%s' % (filename + '1.csv'), 'w', encoding='utf-8', newline='')
            csv_writer = csv.writer(f)
            csv_writer.writerow(self.position[0].keys())
            for item in self.position:
                csv_writer.writerow(item.values())
           


    def inp_sj(self, bj_name, sj_name):
            sj = position[bj_name].get(sj_name)
            self.position_type = sj_name
            bj = position[bj_name]['id']
            return bj, sj

    def run(self, city, bj_name, sj_name, pages):
        bj, sj = self.inp_sj(bj_name, sj_name)
        self.request(bj, sj, pages, city)
        return self.position, self.num



