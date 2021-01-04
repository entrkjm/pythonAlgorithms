import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time



class tableCrawler: #편성표 크롤러 클래스를 만든다

    def __init__(self, chromedriver): #변수로 크롬드라이버 위치를 넣음
        self.chromedriver = chromedriver
        self.driver = webdriver.Chrome(self.chromedriver)

    def get_action(self, title_tag, time_tag, url): #프로그램 이름과 시간을 가져오는 메서드
        self.title_tag = title_tag
        self.time_tag = time_tag
        self.driver.get(url)

        src = self.driver.page_source
        soup = BeautifulSoup(src, features="lxml")

        #pagesource를 가져와서 soup에 넣는다.

        programName = soup.select(title_tag)
        programTime = soup.select(time_tag)

        return programName, programTime

    def reboard_list(self, find_in, find_tag):
        self.find_in = find_in
        self.find_tag = find_tag

        find_in_list = self.driver.find_elements_by_css_selector(self.find_in)
        result = []

        for i in find_in_list:
            if i.find_elements_by_css_selector(self.find_tag):
                result.append('재')
            else:
                result.append('본')

        return result

    def reboard_list2(self, find):
        self.find = find
        find_list = self.driver.find_elements_by_css_selector(self.find)

        result = []

        for i in find_list:
            if i.text.find('스페셜') != -1:
                result.append('재')
            else:
                result.append('본')

        return result

    def driver_close(self):
        self.driver.close()

# 실행 부분
date = input('오늘 날짜를 입력하세요:') #오늘 날짜를 입력

Chromedriver =  'C:/Users/User/PycharmProjects/algorithm1/chromedriver'

# sbs_url = 'https://www.sbs.co.kr/schedule/index.html?type=tv&channel=SBS&pmDate=2021{}'.format('0105')
# sbs = tableCrawler(Chromedriver)
# sbs_title_tag = '.spi_title'
# sbs_time_tag = '.spt_hours'
# sbs_find_in = '.spi_title_icons'
# sbs_find_tag = '.scheduler_label_w_type_rerun'
#
# sbs_programName, sbs_programTime = sbs.get_action(sbs_title_tag, sbs_time_tag, sbs_url)
# sbs_reboard = sbs.reboard_list(sbs_find_in, sbs_find_tag)
#
# for i in range(len(sbs_reboard)):
#     print(sbs_programTime[i].text, sbs_programName[i].text, sbs_reboard[i])

#
# mbc_url = 'http://schedule.imbc.com/?chcode=TV&date=2020{}&c=0'.format(1224)
#
# mbc = tableCrawler(mbc_url)
# mbc_title_tag = '.tit'
# mbc_time_tag = '.time > span'
# mbc_find = '.tit'
#
# mbc_programName, mbc_programTime = mbc.getAction(mbc_title_tag, mbc_title_time)
# mbc_reboard = mbc.reboard_list2(mbc_find)
#
# for i in range(len(mbc_reboard)):
#     print(mbc_programTime[i].text, mbc_programName[i].text, mbc_reboard[i])
#

# KBS 편성표를 가져온다
kbs_url = 'http://schedule.kbs.co.kr/index.html?sname=schedule&stype=table&type=globalList&search_day=2021{}'.format(date)
kbs = tableCrawler(Chromedriver)
kbs_title_tag = 'span.title'
kbs_time_tag = 'span.time'
kbs_programName, kbs_programTime = kbs.get_action(kbs_title_tag, kbs_time_tag, kbs_url)

for i in range(len(kbs_programName)):
    print(kbs_programTime[i].get_text(), kbs_programName[i].get_text())

kbs.driver_close()